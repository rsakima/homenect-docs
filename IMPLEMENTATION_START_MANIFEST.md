# HOMENECT Implementation Start Manifest

基準日: 2026-09-16  
Status: **LOCKED / READY FOR P0 IMPLEMENTATION**

## 最上位・基本実装正本

| 正本 | Version | 用途 |
|---|---:|---|
| Formal Development Order Spec | v2.4 | 最上位実装正本 |
| ERD / DB Design | v1.0 | DB/RLS/Index/Concurrency |
| State Transition / Business Flow | v1.0 | 状態・HELP・Referral・Incident |
| API Spec / OpenAPI | v1.0 / **v1.1** | Route/Contract/Webhook |
| Screen Detail Spec | v1.0 | 入力/表示/権限/Validation |
| Development & Operations Runbook | v1.0 | CI/CD/Deploy/Backup/Incident |

**Machine-readable API正本:** `07_system/openapi/HOMENECT_OpenAPI_v1.1.yaml`

## 追加実装ロック

- [Role / Permission Model v1.0](07_system/30_HOMENECT_Role_Permission_Model_v1.0.md)
- [RBAC Implementation Spec v1.0](07_system/31_HOMENECT_RBAC_Implementation_Spec_v1.0.md)
- [Auth / Account Lifecycle v1.0](07_system/32_HOMENECT_Auth_Account_Lifecycle_v1.0.md)
- [Config Registry v1.0](07_system/33_HOMENECT_Config_Registry_v1.0.md)
- [Notification Event / Template v1.0](07_system/34_HOMENECT_Notification_Event_Template_v1.0.md)
- [Pilot / Production Gate Checklist v1.0](07_system/35_HOMENECT_Pilot_Production_Gate_Checklist_v1.0.md)
- [AI Collaborative Development Protocol v1.0](07_system/36_HOMENECT_AI_Collaborative_Development_Protocol_v1.0.md)

## 人が読む補助資料

- [Development to Production Flow v1.0](07_system/37_HOMENECT_Development_to_Production_Flow_v1.0.md)
  - 「作る → 自動チェック → Staging確認 → Production承認 → 公開」を簡単な日本語で把握する。
  - Gitは `main + 短命branch`、環境は Development / Preview / Staging / Production に分ける。
  - Claude / Codex交代はGit + `docs/AI_HANDOFF.md` を使う。

## Companion / Formal Decisions

- Business Concept Master v2.3
- Requirements Traceability v2.3
- Business Operations Master v2.4
- 案件価格保護・応援施工制度 v1.0

## Role / Permission Lock

- 利用者区分: お客様 / 協力業者 / HOMENECT運営の3グループ
- 内部Role: `customer / partner_admin / technician / ops_admin / finance_admin / compliance_admin / super_admin`
- 1人1アカウント、複数Role兼任可能
- Partner Roleはorganization scope必須
- deny-by-default
- 高リスク操作は自己承認禁止
- 重要操作はAudit必須

## Auth Lock

- 閲覧・空き確認はログイン不要
- `REQUESTED`作成前にCustomer本人確認
- Customer標準はメールOTP、LINEは任意連携
- 電話番号はP0では連絡先であり認証IDにしない
- Partner / Adminは招待制
- `partner_admin` とPlatform AdminはProduction前MFA必須

## API Contract Lock

- **OpenAPI v1.1へ一本化済み**
- `POST /reservations` は本人確認済みSubjectのみ実行可能
- `customer_price_locked` はREQUESTED / MATCHINGではnull可、CONFIRMED以降で必須
- 通常JobOfferは `partner_compensation`、HELP専用報酬は `support_payout`
- v1.0 / Override v1.1は履歴参照のみ

## Config / Notification Lock

- 料金、fee、HELP payout、minimum_margin、offer timeout等はConfig管理
- Config変更を既存予約へ遡及適用しない
- 通知はTransactional Outbox、retry、fallback、dead表示
- 未成約Leadへの有料LINE Pushはdefault deny

## AI共同開発Lock

Claude Desktop / Claude Code / Codexは、Gitを共通記憶として交代可能にする。

- `rsakima/homenect/AI_START_HERE.md` を共通入口にする
- `docs/AI_HANDOFF.md` に現在地を残す
- `docs/AI_DEVELOPMENT_PROTOCOL.md` に共同開発ルールを置く
- 1 PR = 1目的
- 同一branchは同時に1エージェントのみ
- 区切りごとにcommit + push
- 交代前にHandoffを更新
- 次のAIはHandoff / last commit / diff / testsから再開
- Token節約は Search → Minimum Read → Reuse → Minimum Change → Verify → Diff → Handoff

## Deployment Flow Lock

- Gitは `main + 短命feature/fix/chore branch` を基本とし、長期の `dev / staging / main` 3ブランチ運用にはしない。
- mainへ統合した最新版をStagingへ自動デプロイする。
- Product OwnerがStagingをブラウザで確認し、Production公開を承認する。
- ProductionにはStaging確認済みの同一commitをデプロイする。
- DB変更はMigrationで管理し、Staging → Productionの順に適用する。

## GitHub → Google Drive Sync

- GitHubを正式資料のSource of Truthとする。
- `main`更新時に `.github/workflows/sync-google-drive.yml` が対象資料を自動ビルドする。
- MarkdownからWord/PDFを生成し、Drive上の同名ファイルを更新する。
- 同期対象とDrive保存先は `sync/drive-sync.json` で管理する。
- DriveからGitHubへの逆同期はしない。
- Drive上のファイルを自動削除しない。
- Google Drive uploadは初回に `GDRIVE_CLIENT_ID / GDRIVE_CLIENT_SECRET / GDRIVE_REFRESH_TOKEN` をGitHub Secretへ登録後に有効化する。

## Gate Lock

- Pilot前: Partner/Area/保険、Config、RLS/Auth/E2E、通知、Incident、Restore、S1/S2=0を確認
- Production前: 法務、MFA、Security、Monitoring、Backup/Restore、Rollback、Production Config/credentials、Data retention、S1/S2=0を確認

## Readiness

- P0 coding: **READY**
- Tech stack: **LOCKED — Next.js + TypeScript + Supabase**
- Role/Permission model: **LOCKED — 3 groups / 7 roles**
- Auth/account lifecycle: **LOCKED**
- Config registry: **LOCKED**
- Notification event/template: **LOCKED**
- Pilot/Production Gate: **LOCKED**
- API contract: **LOCKED — OpenAPI v1.1 unified**
- Claude/Codex handoff: **LOCKED — Git shared-memory protocol**
- Development → Staging → Production flow: **LOCKED**
- GitHub → Google Drive document sync: **PREPARED — one-time Google OAuth secret setup required**
- Real pricing/payout/minimum_margin: **CONFIG / Pilot前決定**
- Legal review: **Production Gate**
- Initial real Partner/Area/insurance: **Pilot Gate**

## 実装開始ルール

開発者は未確定Business数値を独自判断で固定しない。P0要件・状態遷移・ERD・API・画面・権限・認証・Config・通知・価格保護ルールの変更はChange Requestを経由する。

人が読む資料は難しい表現を避け、日本語主表示・短い説明・具体例を優先する。内部コードやDB用語は開発者向け補足として分離する。
