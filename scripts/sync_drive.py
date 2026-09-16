#!/usr/bin/env python3
import mimetypes
import os
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".sync-output"
SCOPES = ["https://www.googleapis.com/auth/drive"]

MIME = {
    ".md": "text/markdown",
    ".pdf": "application/pdf",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".yaml": "application/yaml",
    ".yml": "application/yaml",
    ".json": "application/json",
}


def esc(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "\\'")


def mime_for(path: Path) -> str:
    return MIME.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or "application/octet-stream"


def credentials():
    required = ["GDRIVE_CLIENT_ID", "GDRIVE_CLIENT_SECRET", "GDRIVE_REFRESH_TOKEN"]
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise SystemExit("Missing required Google Drive credentials: " + ", ".join(missing))
    return Credentials(
        token=None,
        refresh_token=os.environ["GDRIVE_REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.environ["GDRIVE_CLIENT_ID"],
        client_secret=os.environ["GDRIVE_CLIENT_SECRET"],
        scopes=SCOPES,
    )


def find_existing(service, folder_id: str, name: str):
    q = f"'{esc(folder_id)}' in parents and name = '{esc(name)}' and trashed = false"
    result = service.files().list(
        q=q,
        spaces="drive",
        fields="files(id,name,modifiedTime)",
        orderBy="modifiedTime desc",
        pageSize=10,
        supportsAllDrives=True,
        includeItemsFromAllDrives=True,
    ).execute()
    return result.get("files", [])


def upsert(service, path: Path, folder_id: str):
    media = MediaFileUpload(str(path), mimetype=mime_for(path), resumable=False)
    matches = find_existing(service, folder_id, path.name)

    if matches:
        file_id = matches[0]["id"]
        service.files().update(
            fileId=file_id,
            body={"name": path.name},
            media_body=media,
            fields="id,name,modifiedTime",
            supportsAllDrives=True,
        ).execute()
        print(f"UPDATED {path.name} -> {file_id}")
        if len(matches) > 1:
            print(f"WARNING duplicate names exist for {path.name}; updated newest only")
        return

    created = service.files().create(
        body={"name": path.name, "parents": [folder_id]},
        media_body=media,
        fields="id,name,modifiedTime",
        supportsAllDrives=True,
    ).execute()
    print(f"CREATED {path.name} -> {created['id']}")


def main():
    import json

    manifest_path = OUT / "manifest.json"
    if not manifest_path.exists():
        raise SystemExit(".sync-output/manifest.json not found. Run build_drive_docs.py first.")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    service = build("drive", "v3", credentials=credentials(), cache_discovery=False)

    for entry in manifest["files"]:
        path = OUT / entry["path"]
        if not path.exists():
            raise SystemExit(f"Missing built file: {path}")
        upsert(service, path, entry["folder_id"])

    print(f"Drive sync complete: {len(manifest['files'])} files")


if __name__ == "__main__":
    main()
