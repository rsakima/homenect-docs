# HOMENECT 正式資料

HOMENECTの事業・運営・施工・システム・契約に関する正本を管理します。

## 管理ルール
- **GitHub**：Markdown / OpenAPI / Decision / 変更履歴 / 開発仕様の正本。
- **Google Drive**：Word / PDF / Excel / PowerPoint / 画像の完成版。
- 実顧客PII、施工写真、秘密鍵、API KeyはGitHubへ保存しない。
- 料金・報酬・minimum_margin等の変動値はConfigで管理し、コードへ固定しない。
- 契約・法務資料はProduction開始前に専門家確認を行う。

## 現行の実装正本 — 2026-09-16

P0実装開始用の正式6資料をLOCKEDとします。

1. [正式開発発注仕様書 v2.4](07_system/21_HOMENECT_Formal_Development_Order_Spec_v2.4.md)
2. [ER図・DB設計書 v1.0](07_system/25_HOMENECT_ERD_DB_Design_v1.0.md)
3. [状態遷移・業務フロー仕様書 v1.0](07_system/26_HOMENECT_State_Transition_Business_Flow_v1.0.md)
4. [API仕様書 v1.0](07_system/27_HOMENECT_API_Spec_v1.0.md) / [OpenAPI v1.0](07_system/openapi/HOMENECT_OpenAPI_v1.0.yaml)
5. [画面詳細仕様書 v1.0](07_system/28_HOMENECT_Screen_Detail_Spec_v1.0.md)
6. [開発・運用Runbook v1.0](07_system/29_HOMENECT_Development_Operations_Runbook_v1.0.md)

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
- Admin例外操作はRole + reason + Audit必須。
- 利用者・権限は**3グループ・7役割**で管理し、複数役割兼任、組織スコープ、deny-by-default、高リスク自己承認禁止、Auditを適用する。

## 既存正式Decision
- [案件価格保護・応援施工制度](07_system/24_案件価格保護・応援施工制度_正式決定.md)
- [役割・権限モデル v1.0](07_system/30_HOMENECT_Role_Permission_Model_v1.0.md)
- Business Concept Master v2.3（Google Drive完成版）
- Requirements Traceability v2.3（Google Drive完成版）
- Business Operations Master v2.4（Google Drive完成版）

## 人向け資料
既存の事業説明、お客様向け、Partner向け、施工、事故、運営、集客、研修、全国展開、法務資料を継続して使用します。

## Google Drive
HOMENECT root: https://drive.google.com/drive/folders/1XQmsvT1gMUpPvvRxntPF6Z09oGlnE4cm

開発完成版は `15_開発会社向け正式資料/実装開始パッケージ_v1.0` に保存しています。

## 履歴
- [CHANGELOG.md](CHANGELOG.md)
- [IMPLEMENTATION_START_MANIFEST.md](IMPLEMENTATION_START_MANIFEST.md)
