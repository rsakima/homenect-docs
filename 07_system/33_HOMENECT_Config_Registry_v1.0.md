# HOMENECT 設定値一覧 v1.0

**Status: LOCKED / P0**

## 原則
- 料金、fee、support payout、minimum margin、offer timeout、notification policy、area priority、capacityはコードへ固定しない。
- Secret / API KeyはConfig RegistryではなくSecret Manager。
- Config変更はAudit。
- 既存ReservationにはSnapshotを保持し、Config変更を遡及適用しない。

## Registry
| key | 意味 | 初期状態 | 変更権限 |
|---|---|---|---|
| `service_price_rule` | サービス料金 | Pilot前決定 | ops/finance |
| `platform_fee_rule` | HOMENECT手数料 | Pilot前決定 | finance |
| `support_payout_rule` | HELP報酬 | Pilot前決定 | finance |
| `minimum_margin` | HELP最低利益 | Pilot前決定 | finance/super |
| `support_subsidy_limit` | HELP例外補填上限 | Pilot前決定 | finance/super |
| `offer_timeout_minutes` | Offer回答期限 | Pilot前決定 | ops |
| `default_capacity` | 初期capacity | Partnerごと | partner_admin |
| `area_priority_rule` | Areaルーティング | Pilot前決定 | ops |
| `notification_channel_policy` | 通知優先順 | Pilot前決定 | ops |
| `paid_line_unconverted_lead` | 未成約Lead有料LINE | `false` | super |
| `admin_reason_min_chars` | 例外理由最小文字数 | `5` | super |
| `rpo_hours` | RPO目標 | `24` | super |
| `rto_hours` | RTO目標 | `4` | super |
| `media_size_limit` | 画像最大サイズ | 実装時安全値 | super |
