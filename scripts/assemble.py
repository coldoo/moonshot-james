"""Assemble a previz from approved clips (and stills as fallback).

Usage:
    python scripts/assemble.py projects/<name> [options]

Options:
    --slates            add a 1 s scene-id slate before each scene (default: off)
    --overlays          burn the shotlist `overlay` text into each scene (default: off)
    --trim-head S       seconds trimmed from the start of every clip (default 0)
    --trim-tail S       seconds trimmed from the end of every clip (default 0)
    --trim SCENE=H,T    per-scene override, e.g. --trim S01=0.5,0.25 (repeatable)
    --hold S            seconds a still is held when no clip exists (default 5)
    --out NAME          output filename inside <project>/previz/ (default previz.mp4)

Reads:
    <project>/shotlist.json       scene order and overlay text
    <project>/selects.json        `video_selects` (approved clips) and `selects` (approved stills)
    <project>/clips/<id>.mp4      producer-supplied clip, used if no video_select for the scene

Output: 1920x1080, 24 fps, AAC stereo audio. Silent segments get a silent track so the
concat stays in sync.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

W, H, FPS = 1920, 1080, 24
FONT = "C\\:/Windows/Fonts/arial.ttf"
AUDIO = ["-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "192k"]
VIDEO = ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS)]


def find_ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    base = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Packages"
    for p in base.rglob("ffmpeg.exe"):
        return str(p)
    sys.exit("ffmpeg not found")


def probe_duration(ffprobe: str, path: Path) -> float:
    r = subprocess.run([ffprobe, "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", str(path)], capture_output=True, text=True)
    return float(r.stdout.strip())


def esc(text: str) -> str:
    return (text.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’")
            .replace("%", "\\%").replace(",", "\\,"))


def overlay_filter(text: str, start: float) -> str:
    if not text:
        return ""
    return (f",drawtext=fontfile='{FONT}':text='{esc(text)}':fontsize=54:fontcolor=white:"
            f"box=1:boxcolor=black@0.55:boxborderw=22:x=(w-text_w)/2:y=h-200:enable='gte(t,{start})'")


def caption_filters(shot: dict) -> str:
    """Notification (top, phone-banner style) and Moonshot reply (bottom) captions."""
    f = ""
    note = shot.get("notification")
    if note:
        a, b = shot.get("notification_from", 2.0), shot.get("notification_to", 5.0)
        f += (f",drawtext=fontfile='{FONT}':text='{esc(note)}':fontsize=44:fontcolor=white:"
              f"box=1:boxcolor=0x1c1c1e@0.9:boxborderw=26:x=(w-text_w)/2:y=110:"
              f"enable='between(t,{a},{b})'")
    reply = shot.get("reply")
    if reply:
        start = shot.get("reply_at", 5.0)
        lines = reply.split("\n")
        line_h = 76
        base_y = H - 200 - (len(lines) - 1) * line_h
        f += (f",drawtext=fontfile='{FONT}':text='MOONSHOT':fontsize=28:fontcolor=0xd4a24c:"
              f"box=1:boxcolor=black@0.6:boxborderw=12:x=(w-text_w)/2:y={base_y - 68}:enable='gte(t,{start})'")
        for i, line in enumerate(lines):
            f += (f",drawtext=fontfile='{FONT}':text='{esc(line)}':fontsize=54:fontcolor=white:"
                  f"box=1:boxcolor=black@0.6:boxborderw=22:x=(w-text_w)/2:y={base_y + i * line_h}:"
                  f"enable='gte(t,{start})'")
    return f


def run(cmd: list[str]) -> None:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ffmpeg failed:\n{' '.join(cmd)}\n{r.stderr[-3000:]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--slates", action="store_true", help="1 s scene-id card before each scene")
    ap.add_argument("--labels", action="store_true",
                    help="burn the shotlist `label` as a translucent tag over the first seconds of each clip")
    ap.add_argument("--label-cards", action="store_true", help="instead, a 1.2 s black card with the label before each scene")
    ap.add_argument("--label-seconds", type=float, default=2.2, help="how long the translucent tag stays up")
    ap.add_argument("--overlays", action="store_true", help="burn `overlay`, `notification` and `reply` captions")
    ap.add_argument("--trim-head", type=float, default=0.0)
    ap.add_argument("--trim-tail", type=float, default=0.0)
    ap.add_argument("--trim", action="append", default=[], help="SCENE=HEAD,TAIL")
    ap.add_argument("--hold", type=float, default=5.0)
    ap.add_argument("--out", default="previz.mp4")
    args = ap.parse_args()

    per_scene = {}
    for spec in args.trim:
        sid, vals = spec.split("=")
        h, t = (float(x) for x in vals.split(","))
        per_scene[sid] = (h, t)

    proj = Path(args.project)
    ff = find_ffmpeg()
    ffprobe = str(Path(ff).with_name("ffprobe.exe" if ff.endswith(".exe") else "ffprobe"))
    shots = json.loads((proj / "shotlist.json").read_text(encoding="utf-8"))["shots"]
    sel = json.loads((proj / "selects.json").read_text(encoding="utf-8"))
    video_selects = sel.get("video_selects", {})
    still_selects = sel.get("selects", {})
    out_dir = proj / "previz"
    tmp = out_dir / "tmp"
    tmp.mkdir(parents=True, exist_ok=True)

    parts: list[Path] = []
    report = []

    for shot in shots:
        sid = shot["id"]
        overlay = shot.get("overlay") or "" if args.overlays else ""

        card_text = None
        if args.label_cards and shot.get("label"):
            card_text, card_size = shot["label"], 64
        elif args.slates:
            card_text, card_size = sid, 120
        if card_text:
            slate = tmp / f"{sid}_card.mp4"
            run([ff, "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d=1.2",
                 "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", "1.2",
                 "-vf", f"drawtext=fontfile='{FONT}':text='{esc(card_text)}':fontsize={card_size}:fontcolor=white:"
                        f"x=(w-text_w)/2:y=(h-text_h)/2", "-shortest", *VIDEO, *AUDIO, str(slate)])
            parts.append(slate)

        seg = tmp / f"{sid}_seg.mp4"
        clip: Path | None = None
        vs = video_selects.get(sid)
        if vs and vs.get("status") == "approved":
            clip = proj / vs["file"]
        elif (proj / "clips" / f"{sid}.mp4").exists():
            clip = proj / "clips" / f"{sid}.mp4"

        if clip and clip.exists():
            head, tail = per_scene.get(sid, (args.trim_head, args.trim_tail))
            dur = probe_duration(ffprobe, clip)
            length = max(0.5, dur - head - tail)
            hold = float(shot.get("hold", 0)) if args.overlays else 0.0
            vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
                  f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS},format=yuv420p")
            if hold > 0:
                vf += f",tpad=stop_mode=clone:stop_duration={hold}"
            vf += overlay_filter(overlay, 1.0)
            if args.labels and shot.get("label"):
                vf += (f",drawtext=fontfile='{FONT}':text='{esc(shot['label'])}':fontsize=40:fontcolor=white:"
                       f"box=1:boxcolor=black@0.45:boxborderw=18:x=60:y=60:"
                       f"enable='lt(t,{args.label_seconds})'")
            if args.overlays:
                vf += caption_filters(shot)
            af = "aresample=48000" + (f",apad=pad_dur={hold}" if hold > 0 else "")
            run([ff, "-y", "-ss", f"{head:.3f}", "-t", f"{length:.3f}", "-i", str(clip),
                 "-vf", vf, "-af", af, "-t", f"{length + hold:.3f}", *VIDEO, *AUDIO, str(seg)])
            report.append(f"{sid}: clip {clip.name}  {dur:.1f}s -> {length + hold:.1f}s "
                          f"(head {head}, tail {tail}, hold {hold})")
        else:
            ss = still_selects.get(sid, {})
            if ss.get("status") != "approved":
                report.append(f"{sid}: SKIPPED, nothing approved")
                continue
            still = proj / ss["file"]
            frames = int(args.hold * FPS)
            vf = (f"scale=8000:-1,zoompan=z='min(zoom+0.0004,1.08)':d={frames}:"
                  f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},format=yuv420p"
                  + overlay_filter(overlay, 1.0))
            run([ff, "-y", "-loop", "1", "-i", str(still), "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                 "-t", str(args.hold), "-vf", vf, "-shortest", *VIDEO, *AUDIO, str(seg)])
            report.append(f"{sid}: still {still.name} held {args.hold}s")
        parts.append(seg)

    concat = tmp / "concat.txt"
    concat.write_text("".join(f"file '{p.resolve().as_posix()}'\n" for p in parts), encoding="utf-8")
    final = out_dir / args.out
    run([ff, "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(final)])

    total = probe_duration(ffprobe, final)
    print("\n".join(report))
    print(f"wrote {final}  ({total:.1f}s)")


if __name__ == "__main__":
    main()
