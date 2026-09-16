# HOMENECT Implementation Start Manifest

基準日: 2026-09-16  
Status: **LOCKED / READY FOR P0 IMPLEMENTATION**

| 正本 | Version | 用途 |
|---|---:|---|
| Formal Development Order Spec | v2.4 | 最上位実装正本 |
| ERD / DB Design | v1.0 | DB/RLS/Index/Concurrency |
| State Transition / Business Flow | v1.0 | 状態・HELP・Referral・Incident |
| API Spec / OpenAPI | v1.0 | Route/Contract/Webhook |
| Screen Detail Spec | v1.0 | 入力/表示/権限/Validation |
| Development & Operations Runbook | v1.0 | CI/CD/Deploy/Backup/Incident |

## Companion

- Business Concept Master v2.3
- Requirements Traceability v2.3
- Business Operations Master v2.4
- 案件価格保護・応援施工制度 v1.0

## GitHub全文同期

`HOMENECT_Formal_Development_Order_Spec_v2.4.md` の全文同期を完了。

GitHubでは `07_system/21_HOMENECT_Formal_Development_Order_Spec_v2.4.md` を入口とし、本文を下記4ファイルへ順序固定で保存する。

1. `07_system/v2.4/HOMENECT_Formal_Development_Order_Spec_v2.4_part01.md`
2. `07_system/v2.4/HOMENECT_Formal_Development_Order_Spec_v2.4_part02.md`
3. `07_system/v2.4/HOMENECT_Formal_Development_Order_Spec_v2.4_part03.md`
4. `07_system/v2.4/HOMENECT_Formal_Development_Order_Spec_v2.4_part04.md`

単一Markdown原本 SHA-256:
`22df62922ce83b98fcd952d3c299c60930685e93f060a5df517f7cade65506aa`

## Readiness

- P0 coding: **READY**
- Tech stack: **LOCKED — Next.js + TypeScript + Supabase**
- Real pricing/payout/minimum_margin: **CONFIG / Pilot前決定**
- Legal review: **Production Gate**
- Initial real Partner/Area/insurance: **Pilot Gate**

## 実装開始ルール

開発者は未確定Business数値を独自判断で固定しない。P0要件・状態遷移・ERD・API・画面・権限・価格保護ルールの変更はChange Requestを経由する。
