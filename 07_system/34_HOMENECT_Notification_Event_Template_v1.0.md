# HOMENECT 通知ルール v1.0

**Status: LOCKED / P0**

## 原則
- 通知はCore業務トランザクションと分離しTransactional Outboxで送る。
- Provider障害で予約・施工処理を失敗させない。
- 二重送信防止、retry、fallback、dead表示を実装。
- 未成約Leadへの有料LINE Pushはdefault deny。
- 通知本文へ不要PIIを入れない。

## P0 Events
| Event | Recipient | Purpose | Primary |
|---|---|---|---|
| request_received | Customer | 依頼受付 | Email / linked LINE |
| offer_created | Partner | 案件提示 | Email + Partner UI |
| offer_expiring | Partner/Ops | 期限警告 | Email + Admin UI |
| reservation_confirmed | Customer/Partner | 予約確定 | Email / LINE |
| help_requested | Partner/Ops | HELP依頼 | Email + Partner UI |
| help_confirmed | Customer/Partners | HELP成立 | Email / LINE |
| referral_approval_required | Customer | 新業者・新料金承認 | Email / LINE |
| additional_work_approval_required | Customer | 追加料金承認 | Email / LINE |
| incident_reported | Ops/Compliance | 事故初報 | Email + Admin UI |
| notification_dead | Ops | 通知失敗 | Admin UI + Email |
| work_completed | Customer/Partner | 完了 | Email / LINE |
