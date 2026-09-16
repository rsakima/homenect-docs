# HOMENECT 状態遷移・業務フロー仕様書

**Version:** v1.0  
**基準日:** 2026-09-16  
**Status:** LOCKED / P0実装正本

## 1. 目的

「依頼受付」と「予約確定」を混同せず、通常予約、Backup、HELP、完全紹介、追加作業、事故、キャンセルを同じルールで処理する。

![Reservation State Machine](diagrams/HOMENECT_State_Machine_v1.0.png){ width=98% }

## 2. Reservation正式State

| State | お客様表示 | 入口 | 出口 | 禁止事項 |
|---|---|---|---|---|
| REQUESTED | 依頼を受け付けました | 予約作成 | MATCHING/CANCELED | 「予約確定」と表示しない |
| MATCHING | 担当業者を確認しています | REQUESTED | CONFIRMED/CANCELED | PIIを候補業者へ過剰開示しない |
| CONFIRMED | 予約が確定しました | Partner受諾/Referral承認 | HELP_PENDING/IN_PROGRESS/CANCELED | HELPだけで価格変更しない |
| HELP_PENDING | 応援業者を調整しています | CONFIRMED | CONFIRMED/REFERRAL_PENDING/CANCELED | preferred自動変更禁止 |
| REFERRAL_PENDING | 新しい業者・料金を確認してください | HELP_PENDING/Admin開始 | CONFIRMED/CANCELED | Customer未承認で確定しない |
| IN_PROGRESS | 作業中 | CONFIRMED | COMPLETED/INCIDENT_HOLD | 無承認追加作業を課金しない |
| INCIDENT_HOLD | 確認・対応中 | IN_PROGRESS | IN_PROGRESS/COMPLETED/CANCELED | 通常完了を自動実行しない |
| COMPLETED | 完了 | IN_PROGRESS/INCIDENT_HOLD | terminal | 重要証跡の削除禁止 |
| CANCELED | キャンセル | 許可State | terminal | 理由・金銭処理の未記録禁止 |

## 3. Reservation遷移表

| From | To | Trigger | Actor | Guard | Side effects |
|---|---|---|---|---|---|
| - | REQUESTED | create reservation | Customer/System | validation/consent | source記録 |
| REQUESTED | MATCHING | routing start | System | area/service成立 | candidate作成 |
| MATCHING | CONFIRMED | job offer accept | Partner/System | terms snapshot + concurrency | price lock/責任snapshot/通知 |
| MATCHING | CANCELED | no candidate/customer cancel | System/Admin/Customer | reason | cancel policy |
| CONFIRMED | HELP_PENDING | help request | Partner/Admin | reason | price lock維持 |
| HELP_PENDING | CONFIRMED | help accepted | Target Partner/System | margin guard | service_partner変更のみ |
| HELP_PENDING | REFERRAL_PENDING | help impossible/referral | Admin | new candidate | new price draft |
| REFERRAL_PENDING | CONFIRMED | customer approve | Customer/System | price/contract shown | new snapshot有効化 |
| REFERRAL_PENDING | CANCELED | customer reject & no original path | Customer/Admin | reason | notification |
| CONFIRMED | IN_PROGRESS | start work | Service Partner | assigned + date guard | start log |
| IN_PROGRESS | INCIDENT_HOLD | S1/S2 or blocking issue | Partner/System | incident created | completion block |
| INCIDENT_HOLD | IN_PROGRESS | resume | Ops Admin | reason + audit | notification |
| IN_PROGRESS | COMPLETED | complete | Service Partner/System | worklog + test + cash rule | completion notification |
| INCIDENT_HOLD | COMPLETED | corrected completion | Ops Admin/System | resolution | audit |
| allowed | CANCELED | cancellation | Customer/Admin/System | policy | payment/refund record |

## 4. JobOffer State

`offered -> accepted | declined | expired | superseded`

- AcceptはIdempotency-Key + Reservation version必須。
- 最初に有効なAcceptがReservationをCONFIRMEDへ進める。
- 他Offerは`superseded`へ。
- DeclineしてもPartnerへ不利益な自動制裁を行わない。

## 5. HELP State

`requested -> offered -> accepted | declined | expired | canceled`

HELP成立条件：

1. 元ReservationがCONFIRMEDまたはHELP_PENDING。
2. `customer_price_locked`を変更しない。
3. Target Partnerへ`support_payout`を提示。
4. `margin >= minimum_margin`。満たさない場合は自動成立禁止。
5. Accept後、`service_partner_id`のみ必要に応じ更新。
6. `preferred_partner_id`はCustomer希望がない限り維持。

## 6. Referral State

`draft -> pending_customer -> approved | rejected | canceled`

- Referralは契約切替を伴う完全紹介。
- 新業者、新料金、差額、契約主体、保証窓口をCustomerへ表示。
- Customerが承認するまで新条件は有効化しない。

## 7. AdditionalWork State

`proposed -> approved | rejected -> performed | canceled`

- 追加作業は価格を必須入力。
- approved_at前の施工・請求は不可。
- 緊急安全措置は「課金追加作業」ではなくIncident/安全措置として別記録。

## 8. Incident State

`open -> investigating -> action_required -> resolved -> closed`

S1/S2はReservationをINCIDENT_HOLDへ移す。S3/S4は必ずしも停止しないが、Admin Policyで閾値設定する。

## 9. 正常フロー

1. CustomerがWebから依頼。
2. REQUESTED作成。
3. SystemがArea/技能/availability/preferredを評価しMATCHING。
4. JobOfferを候補Partnerへ提示。
5. Partnerが受諾しCONFIRMED。ここで初めて「予約確定」。
6. 必要PIIを施工担当へ開示。
7. 当日IN_PROGRESS。
8. Before/After、test、CashReceiptを記録。
9. 完了条件PassでCOMPLETED。

## 10. Backupフロー

- Offer decline/timeout -> 次候補。
- Customerへ途中の候補業者名を不要に表示しない。
- すべて不成立ならAdmin例外または取消。

## 11. HELPフロー

- 元担当が忙しい/休み/難機種/事故支援等でHELP開始。
- 元予約価格を維持。
- Targetには応援条件だけ提示。
- 成立後も顧客関係は元preferredを維持。
- 採算不成立なら別Target、限定補填、またはReferralへ。

## 12. Timeout基準

実数はConfigだが、`offer_expires_minutes`, `help_offer_expires_minutes`, `customer_referral_approval_expires_hours`をConfig化。期限切れはworkerが処理し、直接DB更新ではなくUse Caseを呼ぶ。

## 13. 状態表示ルール

内部英語StateをそのままCustomerへ出さない。日本語文言は以下を基準とする。

- REQUESTED: 「依頼を受け付けました」
- MATCHING: 「担当業者を確認しています」
- CONFIRMED: 「予約が確定しました」
- HELP_PENDING: 「応援業者を調整しています。料金は確定済みのままです」
- REFERRAL_PENDING: 「新しい業者と料金をご確認ください」
- INCIDENT_HOLD: 「状況を確認し、対応しています」

## 14. 状態変更の監査

Admin例外遷移は`from`, `to`, `actor`, `reason`, `timestamp`, `before/after`をAuditEventへ必須保存。Super Adminも監査削除不可。

## 15. 受入テスト

- Partner受諾前にCustomer画面が「予約確定」にならない。
- HELPで価格が変わらない。
- HELPでpreferredが変わらない。
- Referral承認前にCONFIRMEDへ戻らない。
- 事故Hold中に通常complete APIが拒否される。
- 二重acceptが409になる。
