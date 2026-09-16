# HOMENECT CHANGELOG

HOMENECTの正式資料に関する主な変更履歴です。

## 2026-09-16 — v1.1 案件価格保護・応援施工制度を正式採用

### 正式採用

- **案件価格保護・応援施工制度**をP0として正式採用。
- 応援施工（HELP）と完全紹介（Referral）を分離。
- HELPでは業者変更のみを理由としてお客様の確定済み料金を原則変更しない。
- 応援業者への受託条件をお客様向け通常価格と分離。
- Referralでは新しい業者の料金・条件を事前提示し、お客様承認後に確定。
- 追加作業は内容・追加金額を施工前に承認。
- 赤字・低採算の応援案件を自動成立させないMargin Guardを採用。
- HELPだけではpreferred Partnerを自動変更しない。
- `contract_party` / `payee` / `service_partner` / `warranty_owner` を分離・記録。
- 協力業者同士で最低価格・標準価格・値上げ時期等を共同決定しないガードレールを明文化。

### データ・実装

- `handoff_type = none | help | referral`
- `customer_price_locked`
- `support_payout`
- `platform_fee`
- `support_subsidy`
- `additional_work_approved_at`
- F-033〜F-039を追加。
- R-PP01〜R-PP08、TC-027〜TC-034、AC-21〜AC-28を追加。

### Google Drive 更新

現行正式スナップショットを `98_正式資料一式_v1.1_20260916` として作成。

更新版：
- 総合ハンドブック v1.1
- 総合説明資料 v1.1
- 協力業者募集資料 v1.1
- 人向け関連資料 v1.1
- 法務確認用関連資料 v1.1
- Business Concept Master v2.3
- Formal Development Order Spec v2.2
- Requirements Traceability v2.2
- Business Operations Master v2.3
- 運営管理・普段使う用紙集 v1.1
- 料金・報酬・収益シミュレーション v1.1

### GitHub 更新

- 事業全体説明、1枚資料、Partner参加ルール、毎日の運営、システム、料金・売上を更新。
- お客様利用規約、協力業者契約、個別案件条件、優先担当エリア/応援ルールを更新。
- `07_system/24_案件価格保護・応援施工制度_正式決定.md` を追加。
- Requirements Traceability v2.2 / Business Operations Master v2.3 のDecision Markdownを追加。
- 管理台帳・収益シミュレーションMarkdownをv1.1へ更新。

### 注意

契約・法務資料は法務確認用ドラフトです。実運用前に、契約主体、料金受領者、応援報酬、差額負担、保証・事故・再施工責任、独占禁止法上の運用を専門家確認します。

---

## 2026-09-16 — 完成資料とMarkdown全文同期

- 基本資料15冊を完成版と同期。
- 契約・法務資料7点を追加。
- ブランドルールを追加。
- 事業構想マスター v2.2 と正式開発発注仕様書 v2.1 をMarkdown化。
- 運営管理・用紙集、料金・報酬・収益シミュレーションをMarkdownへ反映。
- `SYNC_MANIFEST.md` を追加。
