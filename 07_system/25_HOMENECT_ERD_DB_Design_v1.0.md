# HOMENECT ER図・DB設計書

**Version:** v1.0  
**基準日:** 2026-09-16  
**Status:** LOCKED / P0実装正本  
**上位文書:** HOMENECT Formal Development Order Spec v2.4

## 1. 目的

この文書は、HOMENECT P0で必要なデータモデル、テーブル責務、制約、RLS、インデックス、監査、画像保存、migration方針を固定する。開発者は、Business Ruleを画面だけで守らずDB制約・RLS・Use Case層で二重に守る。

![HOMENECT ERD](diagrams/HOMENECT_ERD_DB_v1.0.png){ width=98% }

## 2. DB基本方針

- PostgreSQL（Supabase）を正本DBとする。
- UUIDを主キーの標準とする。
- 時刻はDBではUTC `timestamptz`、表示時にAsia/Tokyoへ変換する。
- 金額はJPY整数。浮動小数を使わない。
- 重要なBusiness SnapshotはJSONだけに逃がさず、検索・制約に必要な列を正規化する。
- `created_at`, `updated_at` を業務テーブルに標準付与。監査テーブルは原則append-only。
- 価格・条件・規約versionは後から再現できるようSnapshotを保存する。
- Soft deleteが必要なマスタは`deleted_at`、証跡テーブルは削除しない。

## 3. テーブル一覧

| Table | P0/P1 | 主な責務 |
|---|---:|---|
| subjects | P0 | Core identity |
| external_identities | P0 | LINE等の外部ID連携 |
| customers | P0 | Customer profile |
| equipment | P0 | エアコン等の機器 |
| partners | P0 | 協力業者の事業体 |
| partner_users | P0 | Owner/Technician等 |
| services | P0 | サービスカタログ |
| partner_services | P0 | 対応技能・料金設定参照 |
| area_zones | P0 | 地域Zone |
| partner_areas | P0 | 優先Area/対応可能Area |
| availability_blocks | P0 | 空き・休み・自社予定ブロック |
| customer_relationships | P0 | origin/preferred関係 |
| reservations | P0 | 案件の中心Aggregate |
| reservation_price_snapshots | P0 | 顧客確定価格の履歴 |
| job_offers | P0 | Partnerへの案件提示条件 |
| help_requests | P0 | HELP応援施工 |
| referrals | P0 | 完全紹介・再承認 |
| additional_works | P0 | 追加作業事前承認 |
| work_logs | P0 | 施工記録 |
| media_assets | P0 | 写真メタデータ |
| cash_receipts | P0 | 現金受領記録 |
| incidents | P0 | 事故・トラブル |
| compliance_cases | P0 | 引き抜き等の調査手続き |
| pii_access_events | P0 | 個人情報アクセス証跡 |
| audit_events | P0 | 重要操作監査 |
| notifications | P0 | 通知送信・結果 |
| outbox_events | P0 | Transactional Outbox |
| notification_costs | P1 | 通信費集計 |

## 4. 主要テーブル詳細

### 4.1 reservations

| Column | Type | Null | Rule |
|---|---|---:|---|
| id | uuid | NO | PK |
| customer_id | uuid | NO | FK customers |
| equipment_id | uuid | YES | 初回入力途中を許容する場合のみ |
| service_code | text | NO | services.code |
| requested_slot | timestamptz | NO | Customer希望 |
| status | text/enum | NO | 正式stateのみ |
| handoff_type | text/enum | NO | none/help/referral |
| origin_partner_id | uuid | YES | relationship source |
| preferred_partner_id_snapshot | uuid | YES | 予約時のpreferred |
| service_partner_id | uuid | YES | 実施工業者 |
| customer_price_locked | integer | YES | CONFIRMED以降必須 |
| platform_fee | integer | NO | default 0, Configからsnapshot |
| support_subsidy | integer | NO | default 0, 例外承認のみ |
| minimum_margin_snapshot | integer | YES | HELP判定時の基準 |
| contract_party | text | YES | CONFIRMED以降必須 |
| payee | text | YES | CONFIRMED以降必須 |
| warranty_owner | text | YES | CONFIRMED以降必須 |
| version | integer | NO | optimistic concurrency |
| terms_version | text | NO | 規約version |
| privacy_version | text | NO | privacy version |
| created_at/updated_at | timestamptz | NO | standard |

**Constraint:** HELP中は`customer_price_locked`を変更しない。Referral承認時のみ新PriceSnapshotから更新可能。

### 4.2 job_offers

- `reservation_id`, `partner_id`, `terms_snapshot`, `presented_at`, `expires_at`, `response`, `response_at`。
- `(reservation_id, partner_id, presented_at)`を識別できるようにする。
- Accept時はReservation versionを確認し、既に別Partnerが確定済みなら409。

### 4.3 help_requests

- `requester_partner_id`, `target_partner_id`, `support_payout`, `reason`, `status`, `terms_snapshot`。
- `support_payout`は顧客価格とは別管理。
- Target Partnerには案件受諾に必要な条件のみ表示し、他Partnerの通常価格を表示しない。

### 4.4 referrals

- `from_partner_id`, `to_partner_id`, `new_price_snapshot_id`, `status`, `customer_approved_at`。
- Customer承認前はReservationをCONFIRMEDへ戻さない。
- 承認画面で新業者・新料金・差額・契約主体を表示する。

### 4.5 additional_works

- `description`, `price`, `status`, `approved_at`, `approved_by_subject_id`。
- `approved_at IS NULL`の追加作業をWorkLogの課金対象へ含めない。

### 4.6 customer_relationships

- `source_type`, `origin_partner_id`, `preferred_partner_id`, `updated_reason`, `updated_by`。
- HELP成立のみを理由にpreferredを変更しない。
- Customer本人の変更希望は最優先し、Auditを残す。

### 4.7 audit_events / pii_access_events

`audit_events`は価格、割当、状態、権限、Config、補填、CustomerRelationship変更を記録。`pii_access_events`は詳細住所・電話等の表示/取得を記録する。

## 5. RLS / 権限マトリクス

| Table | Customer | Partner Technician | Partner Owner | Admin |
|---|---|---|---|---|
| customers | own only | assigned reservation必要範囲 | assigned/own-originの必要範囲 | role scope |
| equipment | own only | assigned only | assigned only | role scope |
| reservations | own only | assigned only | own offers/assigned | role scope |
| job_offers | none | own partner only | own partner only | full ops |
| help_requests | none | target/assigned only | requester/target own partner | full ops |
| referrals | own reservation summary | assigned after approval | involved partner | full ops |
| work_logs | own summary read | assigned write | own partner read | ops |
| audit_events | none | none | own minimal when exposed | authorized admin only |
| pii_access_events | none | none | none | security/compliance only |

RLSだけに依存せず、Server APIでownership/assignmentを再検証する。

## 6. Index設計

最低限、以下を作成する。

- `reservations(customer_id, created_at desc)`
- `reservations(status, requested_slot)`
- `reservations(service_partner_id, requested_slot)`
- `job_offers(partner_id, response, expires_at)`
- `partner_areas(zone_id, priority, partner_id)`
- `availability_blocks(partner_id, starts_at, ends_at)`
- `help_requests(target_partner_id, status, created_at)`
- `notifications(status, next_attempt_at)`
- `outbox_events(status, next_attempt_at)`
- `audit_events(entity_type, entity_id, occurred_at desc)`
- `pii_access_events(customer_id, occurred_at desc)`

## 7. 同時実行・二重処理防止

- Reservationの重要遷移は`version`を利用したoptimistic concurrencyまたは`SELECT ... FOR UPDATE`で直列化。
- JobOffer accept / HELP accept / Referral approve / payment recordはIdempotency-Keyを必須化。
- `outbox_events`を同一トランザクションで作成し、DB commit前に外部通知しない。
- 同一Reservationに複数のactive service partnerを作らないDB制約を設ける。

## 8. Storage設計

Private bucket例：`reservation-media`。

`/{environment}/{reservation_id}/{kind}/{uuid}.{ext}`

kindは`equipment`, `before`, `after`, `incident`, `additional_work`等。Public bucketは使用しない。閲覧は短期signed URL + authorization確認。

## 9. Migration / Seed

- `supabase/migrations`をsource of truthとする。
- 本番コンソールでの手作業schema変更は禁止。
- Seedはダミー/マスタ/テストのみ。実顧客PIIをGitへ入れない。
- Migrationはforward-onlyを基本とし、破壊変更はexpand/migrate/contractで段階化。

## 10. Data Retention / Delete

法務確認前の暫定方針：必要最小限の保有期間をConfig/Policyで管理し、監査・契約・事故証跡は業務上必要な期間保有。Customer削除要求時も法令・契約上保持が必要な証跡は匿名化/分離して保持する。具体的期間はProduction Gateで確定。

## 11. DB受入基準

- RLSテストでcross-customer / cross-partner accessが拒否される。
- HELP後も`customer_price_locked`と`preferred_partner_id`が不変。
- Referral承認前は新価格が有効化されない。
- 追加作業承認前は請求対象にならない。
- 二重accept試験でservice partnerが1社に限定される。
- Restore test後にReservation/Relationship/Price Snapshotが再現できる。
