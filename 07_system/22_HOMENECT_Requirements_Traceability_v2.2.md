# HOMENECT Requirements Traceability v2.2

更新日：2026-09-16

## Price Protection / HELP Pricing 追加要件

| Requirement | Feature | Data/API | Test | Acceptance | Priority |
| --- | --- | --- | --- | --- | --- |
| R-PP01 確定価格保護 | F-033 Price Protection | Reservation.customer_price_locked / handoff_type | TC-027 HELPで価格維持 | AC-21 応援変更のみで価格変更なし | P0 |
| R-PP02 応援報酬分離 | F-034 HELP Payout | support_payout / platform_fee / subsidy | TC-028 HELP精算 | AC-22 受託条件と顧客価格分離 | P0 |
| R-PP03 完全紹介再承認 | F-035 Referral Repricing | price_snapshot / customer_approval | TC-029 Referral再価格 | AC-23 新価格承認後のみ確定 | P0 |
| R-PP04 採算ガード | F-036 Margin Guard | margin / exception_state | TC-030 低採算ブロック | AC-24 基準未満は自動成立不可 | P0 |
| R-PP05 追加作業承認 | F-037 Additional Work Approval | additional_work_approved_at | TC-031 追加作業承認 | AC-25 施工前承認必須 | P0 |
| R-PP06 価格協議防止 | F-038 Price Privacy | Partner UI / access control | TC-032 他社通常価格非表示 | AC-26 不要な価格相互開示なし | P0 |
| R-PP07 契約責任再現 | F-039 Responsibility Snapshot | contract_party / payee / service_partner / warranty_owner | TC-033 責任主体再現 | AC-27 後日再現可能 | P0 |
| R-PP08 HELP関係維持 | F-017 HELP + F-033 | preferred_partner_id unchanged by HELP | TC-034 HELP後preferred維持 | AC-28 HELPだけでpreferred変更なし | P0 |

## 実装メモ

- `handoff_type` は `none | help | referral`。
- HELPではCustomer Price Snapshotを維持し、Service Partnerのみ切替可能。
- Referralでは新Price SnapshotとCustomer Approvalを必須化。
- Margin Guardは最低残額基準をConfig化。
- 通常販売価格の相互閲覧は不要。案件遂行に必要な受託条件のみ表示。

同期元：`HOMENECT_Requirements_Traceability_v2.2.xlsx`
