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
- [OpenAPI v1.0](openapi/HOMENECT_OpenAPI_v1.0.yaml)
- [画面詳細仕様書 v1.0](28_HOMENECT_Screen_Detail_Spec_v1.0.md)
- [開発・運用Runbook v1.0](29_HOMENECT_Development_Operations_Runbook_v1.0.md)

## 実装開始判定

**READY FOR P0 IMPLEMENTATION**

- 技術スタック: Next.js + TypeScript + Supabase をLOCK。
- 未確定の料金・Partner報酬・minimum_margin等はConfigとして扱い、Coding Blockerにしない。
- 法務確認はProduction Launch Gateとして継続する。
- 実在Partner / 初期Area / 保険確認等はPilot Gateとして継続する。
