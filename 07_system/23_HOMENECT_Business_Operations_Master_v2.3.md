# HOMENECT Business Operations Master v2.3

更新日：2026-09-16

## 正式決定 D-017：Price Protection / HELP Pricing

| 項目 | 正式方針 |
| --- | --- |
| 通常販売価格 | 各業者が独立して自主的に決定する |
| 応援施工 | お客様の確定価格を原則維持する |
| 完全紹介 | 新しい業者の料金を事前提示し、承認後に切替える |
| 追加作業 | 内容・追加金額を施工前承認する |
| 赤字案件 | 自動成立させない |
| 応援受託条件 | お客様価格と分離して管理する |
| preferred partner | HELPだけでは変更しない |
| 価格協議 | 業者同士で最低価格・標準価格・値上げ時期等を調整しない |

## 保存項目

`handoff_type`, `customer_price_locked`, `support_payout`, `platform_fee`, `support_subsidy`, `additional_work_approved_at`, `contract_party`, `payee`, `service_partner`, `warranty_owner`。

## 例外処理

採算基準を下回る場合は、別応援先、元業者差額負担、限定的なHOMENECT補填、またはReferralによる新料金承認へ分岐します。

## 運営画面

Adminは、価格保護状態、応援報酬、案件残額、例外補填、Referral承認、追加作業承認、責任主体を確認できるようにします。

同期元：`HOMENECT_Business_Operations_Master_v2.3.xlsx`
