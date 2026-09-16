# HOMENECT CHANGELOG

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
