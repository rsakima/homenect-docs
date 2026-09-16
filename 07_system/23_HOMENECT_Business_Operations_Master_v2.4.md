# HOMENECT Business Operations Master v2.4

基準日: 2026-09-16  
Status: LOCKED / P0

Google Drive完成版 `HOMENECT_Business_Operations_Master_v2.4.xlsx` の実装Decision要約。

## 正式ロック

| 項目 | 正式仕様 | Configurable | Coding Guard |
|---|---|---|---|
| Reservation State | REQUESTED/MATCHING/CONFIRMED/HELP_PENDING/REFERRAL_PENDING/IN_PROGRESS/INCIDENT_HOLD/COMPLETED/CANCELED | No | 独自状態追加はChange Request |
| HELP Price | customer_price_locked維持 | No | HELPで顧客価格変更禁止 |
| Support Payout | 案件ごとの受託条件 | Yes | 顧客価格と別保存 |
| Minimum Margin | 採算下限 | Yes | 基準未満は自動成立禁止 |
| Referral Price | 新PriceSnapshot | Yes | Customer承認後のみ有効 |
| Additional Work | 追加作業事前承認 | Yes | approved_atなしで請求不可 |
| Admin Exception | Role + reason + audit | No | Super AdminでもAudit削除不可 |
| Partner Price Privacy | 他社通常価格を常時相互表示しない | No | HELP条件だけ提示 |
| Responsibility | contract_party/payee/service_partner/warranty_owner | No | 完了後も再現可能 |
| Production Legal | 契約主体/責任/差額等の法務確認 | Gate | Coding blockerではない |

## Admin RBAC

| Role | HELP開始 | Referral開始 | 補填承認 | 例外遷移 | 制裁判断 |
|---|---|---|---|---|---|
| Customer | No | No | No | No | No |
| Partner Technician | No | No | No | No | No |
| Partner Owner | Request only | No | No | No | No |
| Ops Admin | Yes | Yes | No | 許可済みのみ | No |
| Finance Admin | No | No | 条件付き | No | No |
| Compliance Admin | No | No | No | case関連のみ | Yes |
| Super Admin | Emergency | Emergency | Emergency | Emergency | Emergency |

Decision D-018: State Machine / ERD / Price Logic / Admin RBAC を2026-09-16にImplementation Lock。
