# HOMENECT 正式開発発注仕様書 v2.4

**Status:** LOCKED / P0実装正本  
**基準日:** 2026-09-16  
**位置づけ:** 見積・設計・実装・テスト・検収の最上位実装正本

Google Driveに保存した `HOMENECT_Formal_Development_Order_Spec_v2.4.md` の全文を、GitHubでは下記4ファイルに順序固定で同期しています。

## 全文

1. [Part 01](v2.4/HOMENECT_Formal_Development_Order_Spec_v2.4_part01.md)
2. [Part 02](v2.4/HOMENECT_Formal_Development_Order_Spec_v2.4_part02.md)
3. [Part 03](v2.4/HOMENECT_Formal_Development_Order_Spec_v2.4_part03.md)
4. [Part 04](v2.4/HOMENECT_Formal_Development_Order_Spec_v2.4_part04.md)

**復元規則:** Part 01 → Part 02 → Part 03 → Part 04 の順に改変せず連結した本文を正式な単一Markdown本文とします。

## 同期検証用 SHA-256

- 単一Markdown原本: `22df62922ce83b98fcd952d3c299c60930685e93f060a5df517f7cade65506aa`
- Part 01: `7cf5e5b2cb6792d3fd1005981519b332341d141d433c96593b9f417709980ee1`
- Part 02: `fc20a051986030946106b1c17ccb1488f8b3a6f345f8bdf054ef387e54947df0`
- Part 03: `b20c2565b6dd6881bb4b5728f5e4a1e7b0f488b69ddcbcf8709e2e1c196bc331`
- Part 04: `e25f2fe24715eacf7ec481316734c5801b0d7ca3130264821a03a032061786d1`

## 実装従属資料

- [ER図・DB設計書 v1.0](25_HOMENECT_ERD_DB_Design_v1.0.md)
- [状態遷移・業務フロー仕様書 v1.0](26_HOMENECT_State_Transition_Business_Flow_v1.0.md)
- [API仕様書 v1.0](27_HOMENECT_API_Spec_v1.0.md)
- [OpenAPI v1.1](openapi/HOMENECT_OpenAPI_v1.1.yaml) **← machine-readable正本**
- [画面詳細仕様書 v1.0](28_HOMENECT_Screen_Detail_Spec_v1.0.md)
- [開発・運用Runbook v1.0](29_HOMENECT_Development_Operations_Runbook_v1.0.md)

`HOMENECT_OpenAPI_v1.0.yaml` と `HOMENECT_OpenAPI_Overrides_v1.1.yaml` は履歴参照用。実装・contract testは統合済み `HOMENECT_OpenAPI_v1.1.yaml` を使用する。

## 追加実装ロック v1.1

以下は2026-09-16に正式採用したP0実装Decisionであり、同一論点について旧記述より優先する。

- [役割・権限モデル v1.0](30_HOMENECT_Role_Permission_Model_v1.0.md)
- [権限実装仕様 v1.0](31_HOMENECT_RBAC_Implementation_Spec_v1.0.md)
- [ログイン・アカウント設計 v1.0](32_HOMENECT_Auth_Account_Lifecycle_v1.0.md)
- [設定値一覧 v1.0](33_HOMENECT_Config_Registry_v1.0.md)
- [通知ルール v1.0](34_HOMENECT_Notification_Event_Template_v1.0.md)
- [Pilot / Production Gate Checklist v1.0](35_HOMENECT_Pilot_Production_Gate_Checklist_v1.0.md)
- [AI共同開発ルール v1.0](36_HOMENECT_AI_Collaborative_Development_Protocol_v1.0.md)

人が読む資料は日本語を主表示とし、「まずここだけ → 一覧 → 必要な補足」の順で簡潔に書く。内部コード・DB名等は開発者向け補足として分離する。

## AI共同開発ロック

Claude Desktop / Claude Code / CodexはGitを共通記憶として交代可能にする。

- 1 PR = 1目的
- 同一branchは同時に1エージェントだけが編集
- 区切りごとにcommit + push
- 中断前に `rsakima/homenect/docs/AI_HANDOFF.md` を更新
- 次のAIはHandoff / last commit / diff / test結果から再開
- チャット履歴を正本にしない
- Token節約のため、必要な仕様だけ最小Readする

## 実装開始判定

**READY FOR P0 IMPLEMENTATION**

- 技術スタック: Next.js + TypeScript + Supabase をLOCK。
- Role/Permission: 3グループ・7役割、複数Role、organization scope、deny-by-defaultをLOCK。
- Customer認証: 閲覧は匿名、予約REQUESTED作成前にメールOTPまたは任意LINE本人確認をLOCK。
- API Contract: **OpenAPI v1.1へ一本化済み**。`POST /reservations`は本人確認済み、`customer_price_locked`はCONFIRMED前null可、通常JobOfferとHELP報酬を分離。
- Config: 料金・fee・HELP payout・minimum_margin等はConfig管理し、既存予約へ遡及しない。
- Notification: Transactional Outbox + retry/fallbackをLOCK。
- Pilot / Production GateをLOCK。
- Claude / Codex共同開発のGit Handoff方式をLOCK。
- 未確定の料金・Partner報酬・minimum_margin等はConfigとして扱い、Coding Blockerにしない。
- 法務確認はProduction Launch Gateとして継続する。
- 実在Partner / 初期Area / 保険確認等はPilot Gateとして継続する。
