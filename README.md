# HOMENECT 正式資料

HOMENECTの事業・運営・施工・システム・契約に関する正本を管理します。

## 管理ルール

- **GitHub**：Markdown / OpenAPI / Decision / 変更履歴 / 開発仕様の正本。
- **Google Drive**：Word / PDF / Excel / PowerPoint / 画像の完成版。
- 実顧客PII、施工写真、秘密鍵、API KeyはGitHubへ保存しない。
- 料金・報酬・minimum_margin等の変動値はConfigで管理し、コードへ固定しない。
- 契約・法務資料はProduction開始前に専門家確認を行う。
- **人が読む資料は難しくしない。日本語主表示・短い説明・具体例を優先し、内部コードやDB用語は開発者向け補足として分離する。**

## 現行の実装正本 — 2026-09-16

### 基本6資料

1. [正式開発発注仕様書 v2.4](07_system/21_HOMENECT_Formal_Development_Order_Spec_v2.4.md)
2. [ER図・DB設計書 v1.0](07_system/25_HOMENECT_ERD_DB_Design_v1.0.md)
3. [状態遷移・業務フロー仕様書 v1.0](07_system/26_HOMENECT_State_Transition_Business_Flow_v1.0.md)
4. [API仕様書 v1.0](07_system/27_HOMENECT_API_Spec_v1.0.md) / **[OpenAPI v1.1](07_system/openapi/HOMENECT_OpenAPI_v1.1.yaml)**
5. [画面詳細仕様書 v1.0](07_system/28_HOMENECT_Screen_Detail_Spec_v1.0.md)
6. [開発・運用Runbook v1.0](07_system/29_HOMENECT_Development_Operations_Runbook_v1.0.md)

### 追加実装ロック

- [役割・権限モデル v1.0](07_system/30_HOMENECT_Role_Permission_Model_v1.0.md)
- [権限実装仕様 v1.0](07_system/31_HOMENECT_RBAC_Implementation_Spec_v1.0.md)
- [ログイン・アカウント設計 v1.0](07_system/32_HOMENECT_Auth_Account_Lifecycle_v1.0.md)
- [設定値一覧 v1.0](07_system/33_HOMENECT_Config_Registry_v1.0.md)
- [通知ルール v1.0](07_system/34_HOMENECT_Notification_Event_Template_v1.0.md)
- [Pilot / Production Gate Checklist v1.0](07_system/35_HOMENECT_Pilot_Production_Gate_Checklist_v1.0.md)
- [AI共同開発ルール v1.0](07_system/36_HOMENECT_AI_Collaborative_Development_Protocol_v1.0.md)

### OpenAPI

実装・SDK生成・contract testでは **`HOMENECT_OpenAPI_v1.1.yaml` のみをmachine-readable正本として使用**する。

`HOMENECT_OpenAPI_v1.0.yaml` と `HOMENECT_OpenAPI_Overrides_v1.1.yaml` は履歴参照用。

### 技術スタックLOCK

- Next.js + TypeScript
- Node.js LTS + pnpm
- Tailwind CSS + design tokens
- Supabase PostgreSQL / Auth / Private Storage
- Next.js Server API + Supabase Edge Functions
- Transactional Outbox + scheduled worker
- LINE Messaging API / LIFF + Email Adapter
- Web PushはP1
- Vitest / Playwright / SQL-RLS tests
- GitHub Actions

### 実装ロック

- REQUESTED / MATCHING / CONFIRMED / HELP_PENDING / REFERRAL_PENDING / IN_PROGRESS / INCIDENT_HOLD / COMPLETED / CANCELED
- HELPでは`customer_price_locked`を維持。
- ReferralはCustomerの新料金承認後のみ確定。
- 追加作業は施工前承認。
- 低採算/赤字HELPは自動成立禁止。
- HELPだけでpreferred Partnerを変更しない。
- Partner間の通常販売価格を常時相互表示しない。
- 利用者・権限は**3グループ・7役割**。1人1アカウント、複数Role、organization scope、deny-by-default、高リスク自己承認禁止、Audit。
- Customerは閲覧時ログイン不要。予約REQUESTED作成前にメールOTPまたは任意LINE本人確認。
- 料金・fee・HELP payout・minimum_margin等はConfig管理し、既存予約へ遡及しない。
- 通知はTransactional Outbox + retry/fallback。
- Pilot / Production Gateを通過してから実利用・本番公開する。

## Claude / Codex共同開発

HOMENECT本体 `rsakima/homenect` ではGitを共通記憶として使用する。

- 共通入口: `AI_START_HERE.md`
- 現在地: `docs/AI_HANDOFF.md`
- 共同開発ルール: `docs/AI_DEVELOPMENT_PROTOCOL.md`
- Claude向け: `CLAUDE.md`
- Codex向け: `AGENTS.md`

同じbranchを同時編集せず、区切りごとにcommit + pushし、交代前にHandoffを更新する。

## 既存正式Decision

- [案件価格保護・応援施工制度](07_system/24_案件価格保護・応援施工制度_正式決定.md)
- Business Concept Master v2.3（Google Drive完成版）
- Requirements Traceability v2.3（Google Drive完成版）
- Business Operations Master v2.4（Google Drive完成版）

## Google Drive

HOMENECT root: https://drive.google.com/drive/folders/1XQmsvT1gMUpPvvRxntPF6Z09oGlnE4cm

開発完成版は `15_開発会社向け正式資料/実装開始パッケージ_v1.0` に保存しています。

## 履歴

- [CHANGELOG.md](CHANGELOG.md)
- [IMPLEMENTATION_START_MANIFEST.md](IMPLEMENTATION_START_MANIFEST.md)
