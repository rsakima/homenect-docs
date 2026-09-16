# HOMENECT 開発・運用Runbook

**Version:** v1.0  
**基準日:** 2026-09-16  
**Status:** LOCKED / P0開発運用正本

## 1. 採用Stack

- Next.js + TypeScript
- pnpm
- Supabase PostgreSQL / Auth / Storage
- Next.js Server API + Supabase Edge Functions
- Tailwind CSS + design tokens
- LINE Messaging API / LIFF Adapter
- Email Provider Adapter
- Transactional Outbox + scheduled worker
- Vitest / Playwright / SQL-RLS tests
- GitHub Actions
- Structured Logs + Sentry等Error Tracking

## 2. Repository構成

```text
homenect/
  apps/web/
    app/
    components/
    features/
    server/
  packages/
    domain/
    ui/
    config/
    api-client/
  supabase/
    migrations/
    functions/
    tests/
  openapi/
  e2e/
  scripts/
  docs/
```

Business Ruleは`packages/domain`または同等Use Case層へ置き、React componentやLINE webhookへ直接埋め込まない。

## 3. Environment

| Env | Data | External Channels | Purpose |
|---|---|---|---|
| local | synthetic only | mock/dev | 開発 |
| development | synthetic | dev credentials | shared dev |
| staging | realistic synthetic | staging LINE/email | E2E/受入 |
| production | real | production credentials | 本番 |

Production dataをlocal/stagingへコピーしない。

## 4. Environment Variables

値はSecret Manager/hosting settingsへ保存し、Gitへ入れない。

```text
NEXT_PUBLIC_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY
SUPABASE_SERVICE_ROLE_KEY
LINE_CHANNEL_SECRET
LINE_CHANNEL_ACCESS_TOKEN
LIFF_ID
EMAIL_PROVIDER_API_KEY
APP_BASE_URL
SENTRY_DSN
OUTBOX_WORKER_SECRET
```

Service Role Keyをbrowserへ露出しない。

## 5. Local Setup

1. Node.js LTS / pnpmを準備。
2. Repository clone。
3. `pnpm install --frozen-lockfile`。
4. Supabase localを起動。
5. `supabase db reset`でmigration + seed。
6. `.env.local`へdev secrets。
7. `pnpm dev`。
8. `pnpm test` / `pnpm e2e`。

## 6. Branch / PR

- `main`: Production-ready。
- feature branch -> PR -> CI -> review -> merge。
- mainへの直接push禁止を推奨。
- 1 PR 1目的。schema/API変更はdocs/OpenAPI同時更新。
- Secrets/real PIIをCommitしない。

## 7. CI Pipeline

PRで必須：

1. install lockfile
2. lint
3. format check
4. TypeScript typecheck
5. unit tests
6. DB migration lint / reset test
7. RLS tests
8. OpenAPI validation
9. build
10. Playwright critical E2E

main merge後：staging deploy -> smoke/E2E -> manual production approval。

## 8. DB Migration

- Schema変更はmigration fileのみ。
- Production SQL consoleで手作業DDL禁止。
- 破壊変更はexpand -> backfill -> switch -> contract。
- migration前にbackup確認。
- migration rollbackが難しい場合はforward fix planをPRに記載。

## 9. Deploy

### Staging

- main mergeで自動deploy。
- migration -> app deployの順序を互換性ある形で設計。
- E2E pass後にProduction candidate tag。

### Production

Release checklist：

- Open P0 S1/S2 defect = 0
- backup latest success
- migration reviewed
- feature flags/config reviewed
- legal/public copy gate satisfied
- Partner/Area initial data confirmed
- monitoring/alert enabled
- rollback owner assigned

## 10. Rollback

App regression: previous deploymentへrollback。DBは原則forward compatible migrationを設計し、app rollbackしても旧schemaと共存できる期間を確保。

## 11. Backup / Restore

P0目標：RPO <= 24h, RTO <= 4h（正式SLAはPilot後再評価）。

Restore drillはPilot前に必須：

1. isolated environmentへrestore。
2. Customer/Reservation/Relationship/PriceSnapshot/Auditの件数・整合性確認。
3. private media参照確認。
4. critical E2E実行。
5. 証跡を保存。

## 12. Monitoring / Alert

監視対象：

- 5xx率
- auth failure異常
- webhook signature failure
- outbox backlog/oldest age
- notification failure率
- JobOffer expiry増加
- DB connection/storage usage
- S1/S2 Incident
- backup failure

Alertは「通知するだけ」ではなく、ownerとrunbook linkを持つ。

## 13. Incident Severity

| Severity | 例 | 初動 |
|---|---|---|
| S1 | PII漏えい、cross-tenant access、広範な本番停止 | 即時。機能停止/credential revokeを含む |
| S2 | 予約二重確定、金額不整合、重要通知大量失敗 | 最優先で封じ込め |
| S3 | 限定的機能不具合、回避策あり | 営業時間内優先 |
| S4 | 軽微UI/文言 | backlog |

## 14. Security Operations

- Admin/Partner Owner MFA。
- least privilege。
- Service key rotation手順を保持。
- 退職/離脱Userは即時disable。
- RLS変更はsecurity review必須。
- Audit/PII access logを通常Adminが削除できない。

## 15. Data Fix

本番データ修正はAdmin UI/approved scriptを優先。直接SQLが必要な場合：ticket/理由/対象件数/backup/peer review/実行者/結果/Auditを残す。

## 16. Notification Operations

Paid LINE Pushは未成約leadへdefault deny。重要通知はPolicyでEmail/LINE等のfallbackを設定。Provider障害時もCore予約処理を失敗させない。

## 17. Outbox Worker

- status: pending/processing/sent/failed/dead。
- retryは指数backoff + jitter。
- max attempts超過はdead letter相当へ移しAdminに表示。
- Workerは同一eventを複数回処理しても副作用が重複しないようidempotentにする。

## 18. Feature Flags / Config

コードへ固定しない値：料金、fee、support payout rule、minimum_margin、offer timeout、notification policy、reminder interval、area priority、capacity。

Config変更はAudit対象。Productionで重要Config変更は二者確認を推奨。

## 19. PII / Logs

ログへ氏名、電話、住所全文、LINE token、Auth token、画像URLの長期signed tokenを出さない。request_id / subject_id / reservation_id等の非秘密識別子を使う。

## 20. Handover

開発会社/AI実装者から最低限受領：

- source repository
- architecture/ERD/API current version
- migrations
- env template（secretなし）
- CI config
- test results
- security verification
- staging/prod deployment procedure
- backup/restore evidence
- known limitations/open issues

## 21. Definition of Done

P0 featureはRequirement -> Feature -> Screen/API -> Test -> AcceptanceがTraceabilityで繋がり、CI/E2E/手動受入をPassし、Runbook更新まで完了して初めてDone。
