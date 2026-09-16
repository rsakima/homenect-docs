# HOMENECT CHANGELOG

## 2026-09-16 — 実装ロック v1.1 正式採用

### 追加ロック
- 権限実装仕様 v1.0：3グループ・7役割を `role_assignments` + organization scopeで実装。
- ログイン・アカウント設計 v1.0：閲覧は匿名、予約REQUESTED作成前に本人確認。Customer標準はメールOTP、LINEは任意連携。
- 設定値一覧 v1.0：料金、fee、HELP payout、minimum_margin、offer timeout等をConfig管理し、コードへ固定しない。
- 通知ルール v1.0：Transactional Outbox + retry/fallback/dead handlingを正式採用。
- Pilot / Production Gate Checklist v1.0：実利用・本番公開前の必須条件を固定。
- 人向け資料は「難しくしない」を正式運用ルール化。日本語主表示、短い説明、具体例、表を優先する。

### 追加資料
- `07_system/31_HOMENECT_RBAC_Implementation_Spec_v1.0.md`
- `07_system/32_HOMENECT_Auth_Account_Lifecycle_v1.0.md`
- `07_system/33_HOMENECT_Config_Registry_v1.0.md`
- `07_system/34_HOMENECT_Notification_Event_Template_v1.0.md`
- `07_system/35_HOMENECT_Pilot_Production_Gate_Checklist_v1.0.md`

---

## 2026-09-16 — 役割・権限モデル v1.0 正式採用

### 正式ロック
- 利用者を **3グループ**（お客様 / 協力業者 / HOMENECT運営）で整理。
- 内部権限を **7役割**（customer / partner_admin / technician / ops_admin / finance_admin / compliance_admin / super_admin）で固定。
- 1人1アカウント・複数Role兼任を正式採用。
- Partner Roleはorganization scope必須。
- deny-by-defaultを認可原則として採用。
- 高リスク操作の自己承認禁止を採用。
- 重要操作のAuditを必須化。
- 優先業者 / 予備業者 / 応援業者 / 専門業者はRBAC Roleではなく案件・Partner関係属性として扱う。
- `07_system/30_HOMENECT_Role_Permission_Model_v1.0.md` を正式Decisionとして追加。

---

## 2026-09-16 — 実装開始パッケージ v1.0 / Development Spec v2.4

### 正式ロック
- P0技術スタックを **Next.js + TypeScript + Supabase** で固定。
- Node.js LTS / pnpm / Tailwind CSS / GitHub Actionsを標準化。
- Transactional Outbox + scheduled workerを通知・期限・retry基盤として採用。
- Reservation State Machineを正式ロック。
- ERD/DB/RLS/Index/Concurrencyルールを正式ロック。
- API契約をOpenAPI 3.1でmachine-readable化。
- Customer / Partner / Adminの画面詳細とPII maskingを固定。
- Dev/Staging/Production、Migration、CI/CD、Backup/Restore、Incident Runbookを固定。

### 追加資料
- `07_system/21_HOMENECT_Formal_Development_Order_Spec_v2.4.md`
- `07_system/25_HOMENECT_ERD_DB_Design_v1.0.md`
- `07_system/26_HOMENECT_State_Transition_Business_Flow_v1.0.md`
- `07_system/27_HOMENECT_API_Spec_v1.0.md`
- `07_system/openapi/HOMENECT_OpenAPI_v1.0.yaml`
- `07_system/28_HOMENECT_Screen_Detail_Spec_v1.0.md`
- `07_system/29_HOMENECT_Development_Operations_Runbook_v1.0.md`

### v2.4 全文同期
- Google Drive上の `HOMENECT_Formal_Development_Order_Spec_v2.4.md` の本文をGitHubへ全文同期。
- GitHub Contents APIの運用上、本文を4分割して順序固定で保存。
- `07_system/21_HOMENECT_Formal_Development_Order_Spec_v2.4.md` を正式入口・復元マニフェストとする。
- 単一Markdown原本 SHA-256: `22df62922ce83b98fcd952d3c299c60930685e93f060a5df517f7cade65506aa`。

### 実装開始判定
P0 codingは開始可能。料金・Partner報酬・minimum_margin等の実数はConfigで後決め可能。法務確認はProduction Gateとして継続。

---

## 2026-09-16 — v1.1 案件価格保護・応援施工制度
- HELPとReferralを分離。
- HELP時の顧客確定価格保護、Margin Guard、追加作業事前承認、責任主体snapshotを正式採用。
- F-033〜F-039 / R-PP01〜R-PP08 / TC-027以降を追加。

---

## 2026-09-16 — 完成資料とMarkdown全文同期
- 基本資料15冊、法務資料、ブランド、事業/開発マスター、管理台帳を同期。
