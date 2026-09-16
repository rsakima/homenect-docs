# HOMENECT 画面詳細仕様書

**Version:** v1.0  
**基準日:** 2026-09-16  
**Status:** LOCKED / P0実装正本

![Screen Map](diagrams/HOMENECT_Screen_Map_v1.0.png){ width=98% }

## 1. 共通UXルール

- Customer/PartnerはMobile First。AdminはDesktop First。
- Customerには難しい内部用語を出さない。
- 「依頼受付」と「予約確定」を明確に分ける。
- 金額は予約確定/Referral/追加作業の各承認時に、合計と追加条件を明示。
- 破壊的操作は確認画面または二段階確認。
- エラーは「何が起きたか + 次に何をすればよいか」を表示。
- PartnerにはAccept前に不要PIIを表示しない。
- 重要なAudit対象操作は理由入力を必須化。

## 2. Customer Screen

### CUS-001 サービス・料金・対応地域

**目的:** 初回のお客様が、LINEなしでサービス内容・料金の考え方・対応地域を理解し、予約へ進む。

**表示:** サービス名、料金/参考価格またはPartner別価格、追加料金条件、対応地域、キャンセル概要、FAQ。  
**CTA:** `予約する`。  
**Validation:** なし。  
**Analytics:** `service_view`, `booking_start`。

### CUS-002 機器・写真入力

| 項目 | 必須 | Rule |
|---|---:|---|
| エアコン種類 | Yes | 通常/お掃除機能/不明 |
| メーカー | No | 不明可 |
| 型番 | No | 不明可 |
| 部屋 | No | 自由入力 |
| 写真 | 条件付 | 型番不明等の場合推奨/Policyで必須可 |

Upload失敗は再試行可能。途中入力を安全に保持する。

### CUS-003 空き・料金確認

地域、希望日、台数、機種条件から候補枠を表示。即時確定ではなく、初期は`依頼受付`が標準。完全に事前承認された枠のみ将来`instant_if_preapproved`を許可。

### CUS-004 最終確認

**必須表示:** サービス、台数、予定総額、追加料金条件、希望日時、支払方法、契約主体、キャンセル条件、規約/Privacy version。  
**Button:** `この内容で依頼する`。  
**完了表示:** 「依頼を受け付けました。担当業者を確認しています。」

### CUS-005 予約詳細

表示: 状態、日時、料金、担当/施工業者、契約主体、支払先、保証窓口、キャンセル可否。HELP時は「応援施工に変わっても確定済み料金は原則変わりません」と表示。

### CUS-006 LINE連携

任意。LIFF tokenをServer verifyし、既存CustomerへExternalIdentityをリンク。重複Customerを作らない。

### CUS-008 優先担当変更

Customer本人が「今後は別業者」「優先担当を解除」を依頼可能。変更理由は任意、システム側はactor/timeをAudit。

### CUS-009 完全紹介・再承認

**必須表示:** 新業者名、新料金、元料金との差額、契約主体、支払先、保証窓口、選択肢。  
**Buttons:** `この条件でお願いする` / `今回はお願いしない`。  
承認前にCONFIRMEDへ戻さない。

### CUS-010 追加作業承認

追加内容と追加金額を1件ずつ表示。`承認する/断る`。承認時刻を保存。

## 3. Partner Screen

### PAR-001 Partner Home

受付ON/OFF、今日の案件、未回答Offer、HELP、事故/要対応を優先表示。技術指標より「今やること」を先に出す。

### PAR-002 Job Offer

**Accept前表示:** 日時、概算地域、作業内容、機種/台数、報酬/受託条件、支払条件、期限。  
**非表示:** 不要な氏名フル、電話、詳細住所。  
**Buttons:** `受ける` / `断る`。

### PAR-003 今日の案件

時系列一覧。移動時間/予備時間を含める。自社予定は「予定あり」としてCustomer PIIなしでもブロック登録可能。

### PAR-004 作業報告

開始、Before写真、作業項目、異常、After写真、試運転、完了、現金受領。Incidentがblockingの場合は通常完了Buttonを無効化。

### PAR-005 HELP

依頼側: 理由（繁忙/休み/難機種/技術支援/事故/その他）、希望時間。  
応援側: 案件情報、`support_payout`、期限。**他社の通常販売価格は表示しない。**

### PAR-006 稼働・予定

受付ON/OFF、capacity、時間枠、休み、自社予定ブロック。自社顧客の氏名/電話は入力不要。

### PAR-008 事故・サポート

Severity、種類、状況、Customer安全、写真、HOMENECTへ連絡。返金等を現場で勝手に確約しない旨を表示。

## 4. Admin Screen

### ADM-001 Dashboard

未割当、期限切れ間近Offer、HELP、Incident、Referral承認待ち、低採算例外、通知失敗を「要対応」として表示。

### ADM-002 Reservations

検索: status, date, area, partner, customer, handoff_type。詳細ではState timelineとPrice/Responsibility snapshotを表示。

### ADM-003 Customer / Equipment

Customer基本情報、機器、履歴、CustomerRelationship。PII表示操作はAccess Audit対象。

### ADM-004 Partner / Area

Partner状態、技能、保険/資格期限、Area priority、capacity。優先Areaは独占表示にしない。

### ADM-005 Notification Policy

Eventごとの優先Channel、Fallback、Paid LINE許可/禁止、rate/cost classをConfig。

### ADM-006 Incident / Audit

Incident timeline、証拠、対応方針。Auditは変更不可。検索/Exportは権限者のみ。

### ADM-008 Compliance Case

申告、証拠、Partner回答、Human Decision、段階的措置。1件の申告だけで自動banしない。

### ADM-009 Price / Exception

表示: customer_price_locked, support_payout, platform_fee, variable_cost, subsidy, margin, minimum_margin, handoff, contract/payee/service/warranty。  
補填/例外遷移はRole + reason必須。Partner通常価格の横並び比較画面を作らない。

## 5. Validation共通

- 金額 < 0は禁止（refund等は別Transactionで表現）。
- 日時のend <= startは禁止。
- 画像size/MIME制限。
- Referral approveは新PriceSnapshot必須。
- AdditionalWork approveはprice > 0、description必須。
- Admin reasonは最低文字数をConfig（初期5文字）。

## 6. Error UI

| Error | Customer/Partner表示 | 内部Code例 |
|---|---|---|
| Offer expired | 「この案件は受付期限を過ぎました」 | OFFER_EXPIRED |
| State conflict | 「状態が更新されました。再読み込みしてください」 | RESERVATION_STATE_CONFLICT |
| No permission | 「この操作はできません」 | FORBIDDEN |
| Upload failed | 「写真の送信に失敗しました。もう一度お試しください」 | MEDIA_UPLOAD_FAILED |
| Margin block | Partnerには「この条件では成立できません。別候補を調整します」 | MARGIN_GUARD_BLOCKED |

## 7. Accessibility

WCAG 2.2 AAを目標。十分なcontrast、44px相当tap target、keyboard focus、form label、画像alt、エラーとfieldの関連付けを実装。

## 8. Screen受入基準

- CUS-004で確定前に「予約確定」と出ない。
- CUS-009で新料金差額が明確。
- PAR-002でAccept前PIIがmask。
- PAR-005で他社通常価格が非表示。
- ADM-009の補填/例外にreasonとAuditが必須。
- Customer/Partner主要画面が390px幅で操作可能。
