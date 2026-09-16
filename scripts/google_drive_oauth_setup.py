#!/usr/bin/env python3
import argparse

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/drive"]


def main():
    parser = argparse.ArgumentParser(description="Generate Google Drive refresh token for HOMENECT GitHub Actions")
    parser.add_argument("--client-id", required=True)
    parser.add_argument("--client-secret", required=True)
    args = parser.parse_args()

    config = {
        "installed": {
            "client_id": args.client_id,
            "client_secret": args.client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"],
        }
    }

    flow = InstalledAppFlow.from_client_config(config, SCOPES)
    creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")

    if not creds.refresh_token:
        raise SystemExit("Refresh token was not returned. Retry with prompt=consent or review OAuth app settings.")

    print("\nAdd these GitHub Actions secrets to rsakima/homenect-docs:\n")
    print(f"GDRIVE_CLIENT_ID={args.client_id}")
    print(f"GDRIVE_CLIENT_SECRET={args.client_secret}")
    print(f"GDRIVE_REFRESH_TOKEN={creds.refresh_token}")
    print("\nDo not commit these values to Git.\n")


if __name__ == "__main__":
    main()
