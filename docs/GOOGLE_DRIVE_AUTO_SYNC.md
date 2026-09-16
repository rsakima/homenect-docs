# HOMENECT Google Drive自動同期

## まずここだけ

GitHubの正式資料を更新して`main`へ入れると、Google Drive用のMarkdown / Word / PDFを自動生成する仕組みを追加しています。

Google Driveへの自動保存を有効にするには、**初回だけGoogle認証を3つのGitHub Secretへ登録**します。

一度登録すれば、その後は通常操作は不要です。

```text
Claude / CodexがGitHubの正式資料を更新
        ↓
mainへ反映
        ↓
GitHub Actionsが自動実行
        ↓
Markdown / Word / PDFを自動生成
        ↓
同名ファイルがDriveにあれば更新
        ↓
なければ新規作成
```

## 自動同期するもの

- 正式開発発注仕様書
- ER図・DB設計
- 状態遷移・業務フロー
- API仕様
- 画面詳細仕様
- 開発・運用Runbook
- 役割・権限
- 認証・Config・通知・Gate
- AI共同開発ルール
- 開発から公開までの流れ
- README / Manifest / CHANGELOG
- OpenAPI v1.1

対象一覧は `sync/drive-sync.json` で管理します。

## 安全ルール

- GitHubを正本にします。
- DriveからGitHubへは逆同期しません。
- Drive上の同名ファイルは更新します。
- Drive上のファイルを自動削除しません。
- Secret、API Key、実顧客PIIは同期対象にしません。
- PRではDrive Secretを使わず、`main`反映後だけ同期します。

## 初回だけ必要な設定

### 1. Google CloudでDrive APIを有効にする

Google Cloud Consoleで任意のProjectを作り、Google Drive APIを有効にします。

### 2. OAuth Clientを1つ作る

「Desktop app」のOAuth Clientを作成します。

取得するのは次の2つです。

- Client ID
- Client Secret

### 3. Refresh Tokenを作る

PCでこのRepositoryを開き、次を実行します。

```bash
python -m pip install google-auth-oauthlib
python scripts/google_drive_oauth_setup.py \
  --client-id "YOUR_CLIENT_ID" \
  --client-secret "YOUR_CLIENT_SECRET"
```

ブラウザでGoogle Driveへのアクセスを許可すると、Refresh Tokenが表示されます。

### 4. GitHub Secretsへ登録

`rsakima/homenect-docs` の Actions secrets に次の3つを登録します。

- `GDRIVE_CLIENT_ID`
- `GDRIVE_CLIENT_SECRET`
- `GDRIVE_REFRESH_TOKEN`

値はGitへcommitしません。

### 5. 動作確認

GitHub Actionsの `Sync formal docs to Google Drive` を手動実行します。

成功後は、正式資料を`main`へ更新するたびに自動同期されます。

## 補足

Google OAuthの同意画面をTestingのまま使うとRefresh Tokenが短期間で失効する場合があります。個人利用で継続同期する場合は、OAuth設定を継続利用できる状態にしてから運用します。

Google Driveの保存先は現在のHOMENECT実装開始パッケージです。OpenAPIだけは既存の`openapi`サブフォルダへ同期します。
