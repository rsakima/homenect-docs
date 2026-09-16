# HOMENECT Implementation Start Manifest

基準日: 2026-09-16  
Status: **LOCKED / READY FOR P0 IMPLEMENTATION**

## 最上位・基本実装正本

| 正本 | Version | 用途 |
|---|---:|---|
| Formal Development Order Spec | v2.4 | 最上位実装正本 |
| ERD / DB Design | v1.0 | DB/RLS/Index/Concurrency |
| State Transition / Business Flow | v1.0 | 状態・HELP・Referral・Incident |
| API Spec / OpenAPI | v1.0 + Override v1.1 | Route/Contract/Webhook |
| Screen Detail Spec | v1.0 | 入力/表示/権限/Validation |
| Development & Operations Runbook | v1.0 | CI/CD/Deploy/Backup/Incident |

## 追加実装ロック v1.1

- [Role / Permission Model v1.0](07_system/30_HOMENECT_Role_Permission_Model_v1.0.md)
- [RBAC Implementation Spec v1.0](07_system/31_HOMENECT_RBAC_Implementation_Spec_v1.0.md)
- [Auth / Account Lifecycle v1.0](07_system/32_HOMENECT_Auth_Account_Lifecycle_v1.0.md)
- [Config Registry v1.0](07_system/33_HOMENECT_Config_Registry_v1.0.md)
- [Notification Event / Template v1.0](07_system/34_HOMENECT_Notification_Event_Template_v1.0.md)
- [Pilot / Production Gate Checklist v1.0](07_system/35_HOMENECT_Pilot_Production_Gate_Checklist_v1.0.md)
- [OpenAPI Overrides v1.1](07_system/openapi/HOMENECT_OpenAPI_Overrides_v1.1.yaml)

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

## API Contract Clarification

- `POST /reservations` は本人確認済みSubjectのみ実行可能
- `customer_price_locked` はREQUESTED / MATCHINGではnull可、CONFIRMED以降で必須
- 通常JobOfferは `partner_compensation`、HELP専用報酬は `support_payout`
- Full OpenAPI v1.0には `HOMENECT_OpenAPI_Overrides_v1.1.yaml` を必ず適用する

## Config / Notification Lock

- 料金、fee、HELP payout、minimum_margin、offer timeout等はConfig管理
- Config変更を既存予約へ遡及適用しない
- 通知はTransactional Outbox、retry、fallback、dead表示
- 未成約Leadへの有料LINE Pushはdefault deny

## Gate Lock

- Pilot前: Partner/Area/保険、Config、RLS/Auth/E2E、通知、Incident、Restore、S1/S2=0を確認
- Production前: 法務、MFA、Security、Monitoring、Backup/Restore、Rollback、Production Config/credentials、Data retention、S1/S2=0を確認

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
- Role/Permission model: **LOCKED — 3 groups / 7 roles**
- Auth/account lifecycle: **LOCKED**
- Config registry: **LOCKED**
- Notification event/template: **LOCKED**
- Pilot/Production Gate: **LOCKED**
- API contract override: **LOCKED**
- Real pricing/payout/minimum_margin: **CONFIG / Pilot前決定**
- Legal review: **Production Gate**
- Initial real Partner/Area/insurance: **Pilot Gate**

## 実装開始ルール

開発者は未確定Business数値を独自判断で固定しない。P0要件・状態遷移・ERD・API・画面・権限・認証・Config・通知・価格保護ルールの変更はChange Requestを経由する。

人が読む資料は難しい表現を避け、日本語主表示・短い説明・具体例を優先する。内部コードやDB用語は開発者向け補足として分離する。
