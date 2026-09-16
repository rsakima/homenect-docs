#!/usr/bin/env python3
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "sync" / "drive-sync.json"
OUT = ROOT / ".sync-output"
CSS = ROOT / "scripts" / "drive-sync.css"


def run(cmd):
    print("+", " ".join(map(str, cmd)))
    subprocess.run([str(x) for x in cmd], check=True)


def load_text(entry):
    if "sources" in entry:
        parts = []
        for src in entry["sources"]:
            p = ROOT / src
            parts.append(p.read_text(encoding="utf-8").rstrip())
        return "\n\n".join(parts) + "\n"
    return (ROOT / entry["source"]).read_text(encoding="utf-8")


def main():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    manifest = []

    for entry in cfg["documents"]:
        text = load_text(entry)
        base = entry["basename"]
        folder_id = cfg["drive_folders"][entry["folder"]]
        md = OUT / f"{base}.md"
        md.write_text(text, encoding="utf-8")

        for fmt in entry.get("formats", []):
            target = OUT / f"{base}.{fmt}"
            if fmt == "md":
                pass
            elif fmt == "docx":
                run(["pandoc", md, "--from=gfm", "--to=docx", "-o", target])
            elif fmt == "pdf":
                html = OUT / f"{base}.html"
                run([
                    "pandoc", md, "--from=gfm", "--to=html5", "--standalone",
                    "--metadata", f"title={base}", "-o", html
                ])
                run(["weasyprint", html, target, "--stylesheet", CSS])
                html.unlink(missing_ok=True)
            else:
                raise ValueError(f"Unsupported format: {fmt}")
            manifest.append({"path": target.name, "folder_id": folder_id})

    for entry in cfg.get("raw_files", []):
        src = ROOT / entry["source"]
        target = OUT / entry["name"]
        shutil.copy2(src, target)
        manifest.append({
            "path": target.name,
            "folder_id": cfg["drive_folders"][entry["folder"]]
        })

    (OUT / "manifest.json").write_text(
        json.dumps({"files": manifest}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Built {len(manifest)} files into {OUT}")


if __name__ == "__main__":
    main()
