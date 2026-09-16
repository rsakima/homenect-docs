# HOMENECT API仕様書

**Version:** v1.0  
**基準日:** 2026-09-16  
**Status:** LOCKED / P0実装正本  
**Machine-readable:** `openapi/HOMENECT_OpenAPI_v1.0.yaml`

## 1. 目的

Customer / Partner / Admin / LINE等の境界をAPIとして固定し、画面実装からBusiness Ruleを分離する。実装はOpenAPIとこの文書の両方を満たす。

## 2. 共通規約

- Base path: `/api/v1`
- Content-Type: `application/json; charset=utf-8`
- Auth: Supabase Auth JWT Bearer。公開endpointを除く。
- 日時: ISO 8601 UTC。ClientでAsia/Tokyo表示。
- 金額: JPY integer。
- ID: UUID。
- 重要なPOST: `Idempotency-Key`必須。
- 同時更新: `expected_version`またはIf-Match相当で競合検出。
- 監査対象操作はServer側でactor/reasonを保存。Client送信actorを信用しない。

## 3. Error Envelope

```json
{
  "error": {
    "code": "RESERVATION_STATE_CONFLICT",
    "message": "現在の状態ではこの操作を実行できません。",
    "request_id": "req_xxx",
    "details": {"current_state": "COMPLETED"}
  }
}
```

主要HTTP status: 400 validation / 401 unauthenticated / 403 forbidden / 404 / 409 concurrency-state conflict / 422 business-rule rejection / 429 / 500。

## 4. Customer API

| Method | Path | 目的 | 重要Guard |
|---|---|---|---|
| GET | `/availability` | 空きと概算料金 | 公開可、rate limit |
| POST | `/reservations` | REQUESTED作成 | consent/validation/idempotency |
| GET | `/reservations/{id}` | 自分の予約 | ownership |
| POST | `/reservations/{id}/cancel` | 取消 | policy/state |
| POST | `/identity/line/link` | LINE任意連携 | LIFF token server verify |
| POST | `/customer/preferred-partner/change-request` | preferred変更依頼 | Customer choice audit |
| POST | `/referrals/{id}/approve` | 完全紹介承認 | new price/contract snapshot |
| POST | `/referrals/{id}/reject` | 完全紹介拒否 | ownership |
| POST | `/additional-work/{id}/approve` | 追加作業承認 | amount snapshot |
| POST | `/additional-work/{id}/reject` | 追加作業拒否 | ownership |

## 5. Partner API

| Method | Path | 目的 | 重要Guard |
|---|---|---|---|
| GET | `/partner/offers` | Offer一覧 | own partner |
| POST | `/partner/offers/{id}/accept` | 受諾 | idempotency + version + expiry |
| POST | `/partner/offers/{id}/decline` | 辞退 | own offer |
| PUT | `/partner/availability` | 空き/休み/受付状態 | own partner |
| POST | `/reservations/{id}/help` | HELP依頼 | assigned/owner + reason |
| POST | `/help/{id}/accept` | HELP受諾 | payout snapshot + margin guard |
| POST | `/help/{id}/decline` | HELP辞退 | target partner |
| POST | `/worklogs` | 施工記録 | assigned technician |
| POST | `/cash-receipts` | 現金受領 | reservation relation |
| POST | `/incidents` | 事故報告 | assigned actor |
| POST | `/additional-work` | 追加作業提案 | assigned actor |

## 6. Admin API

| Method | Path | 目的 | Role |
|---|---|---|---|
| GET | `/admin/reservations` | 検索/一覧 | Ops |
| POST | `/admin/reservations/{id}/transition` | 例外遷移 | Ops/Super + reason |
| POST | `/admin/reservations/{id}/referral` | 完全紹介開始 | Ops |
| POST | `/admin/subsidies/{reservation_id}/approve` | 例外補填 | Finance/Super |
| GET | `/admin/partners` | Partner管理 | Ops |
| GET | `/admin/areas` | Area管理 | Ops |
| GET/PUT | `/admin/notification-policy` | 通知Policy | Authorized Admin |
| GET | `/admin/incidents` | 事故管理 | Ops |
| GET | `/admin/compliance-cases` | Compliance | Compliance |
| GET | `/admin/audit` | Audit検索 | Authorized Admin |

## 7. Idempotency

対象：reservation create, offer accept, help accept, referral approve, additional-work approve, cash receipt, outbound notification。

Serverは `(subject_id, method, path, idempotency_key)` を一定期間保存し、同じkeyの再送では同じ結果を返す。payload hashが異なる同keyは409。

## 8. PII段階開示

- Offer前/Offer中: 氏名フル、電話、番地以下を原則非表示。概算Areaと作業情報のみ。
- Accept後: 施工に必要な住所・連絡先のみ。
- PII返却APIは`PIIAccessEvent`を作成。
- HELP TargetもAccept前は同じマスキング。

## 9. Webhook / LINE

`POST /webhooks/line`はLINE signatureをServer側検証。Clientから渡されたLINE userIdをそのまま信用しない。Webhookは受信イベントをidempotentに処理し、業務処理はCore Use Caseへ委譲する。

## 10. Outbox / Notification

DB transaction内で`outbox_events`を作成し、workerがLINE/Email/Web Push adapterへ送信。Provider失敗時は指数backoff + max attempts。Paid LINE Push to unconverted leadはPolicyでdefault deny。

## 11. Security Header / Abuse

- CSRF/XSS/CSPをFramework推奨に沿って設定。
- Public availability / reservation create / uploadにrate limit。
- File uploadはMIME/size/authをServer検証。
- Admin/Partner OwnerはMFAをProduction Gateとする。

## 12. API受入条件

- OpenAPI validationがCIでPass。
- API contract testがPass。
- 不正なstate transitionは422/409。
- cross-tenant accessは403。
- PII before acceptはmask。
- Help acceptでmargin guardが動作。
- Referral承認前の確定を拒否。

## 13. OpenAPIの扱い

`HOMENECT_OpenAPI_v1.0.yaml`をmachine-readable sourceとし、route実装・SDK生成・contract testの基準にする。API変更はOpenAPIを先に変更し、Change Request/PRでレビューする。
