| F-010       | Preferred Area router                     | P07          | P0           |
| F-011       | Preferred Partner continuity              | P08          | P0           |
| F-012       | Job offer / terms snapshot                | P03          | P0           |
| F-013       | Accept/decline + expiry                   | P04          | P0           |
| F-014       | Overflow/Backup queue                     | P09          | P0           |
| F-015       | Work log / photos                         | P05          | P0           |
| F-016       | Cash receipt                              | P06          | P0           |
| F-017       | HELP request                              | P10          | P0           |
| F-018       | Notification Engine                       | A03,S06      | P0           |
| F-019       | LINE adapter / LIFF entry                 | C05,S06      | P0           |
| F-020       | Email adapter                             | A03,S06      | P0           |
| F-021       | Audit / Incident                          | S02,S05      | P0           |
| F-022       | Backup/Restore                            | S04          | P0           |
| F-023       | Admin Console                             | A01,A02,A03  | P0           |
| F-024       | PWA/Web Push                              | P11          | P1           |
| F-025       | Repeat / same-as-before                   | C06,C07      | P1           |
| F-026       | Communication Cost Ledger                 | A04          | P1           |
| F-027       | KPI Dashboard                             | A05          | P1           |
| F-028       | Customer relationship source & continuity | C08,P12      | P0           |
| F-029       | Anti-circumvention policy engine          | P13,A06      | P0           |
| F-030       | Staged PII disclosure                     | S07          | P0           |
| F-031       | Compliance case management                | A06,S08      | P0           |
| F-032       | Contact/assignment access audit           | S08          | P0           |

# 06-A / Relationship Protection & Anti-Circumvention

目的は「顧客を囲い込むこと」ではなく、HOMENECTが生み出した顧客接点・案件情報の不正な迂回利用を防ぎながら、顧客の選択権とPartnerの独立性を守ること。P0としてデータ、権限、監査、Compliance Workflowを実装する。

- CustomerRelationship に source_type / origin_partner_id / preferred_partner_id を保持し、Reservation/WorkLog側の実施工Partnerと分離する。

- Partner案件提示段階では顧客のPIIをマスクし、受諾後に業務上必要な範囲だけ開示する。

- 電話番号・詳細住所等のPII閲覧は理由/actor/timeを監査可能にする。

- ComplianceCase は allegation / evidence / partner_response / decision / action / status を保持し、申告だけで自動制裁しない。

- 措置は警告→新規案件配信停止→Preferred資格停止→契約解除等の段階制を想定し、具体条件はConfig/契約で確定する。

- 顧客本人がPartner変更を希望する場合は、禁止条項で妨げず、変更/解除を可能にする。

# 07 / 画面一覧・画面仕様

| **Screen ID** | **画面**        | **Role**   | **主CTA**                      |
|---------------|-----------------|------------|--------------------------------|
| CUS-001       | サービス/料金   | Customer   | 予約へ                         |
| CUS-002       | 機器・写真      | Customer   | 次へ                           |
| CUS-003       | 空き枠          | Customer   | 候補選択                       |
| CUS-004       | 予約確認        | Customer   | 確定                           |
| CUS-005       | 予約一覧/詳細   | Customer   | 変更/取消                      |
| CUS-006       | LINE連携        | Customer   | 任意連携                       |
| CUS-007       | 再予約          | Customer   | 前回と同じ(P1)                 |
| PAR-001       | Partner Home    | Partner    | 受付ON/OFF                     |
| PAR-002       | 案件オファー    | Partner    | 受諾/辞退                      |
| PAR-003       | 今日の仕事      | Technician | 案件を開く                     |
| PAR-004       | 作業報告        | Technician | 開始/完了                      |
| PAR-005       | HELP            | Partner    | 要請作成/応答                  |
| PAR-006       | スケジュール    | Partner    | 空き/休み                      |
| PAR-007       | 売上/精算       | Partner    | 確認(P1)                       |
| ADM-001       | Dashboard       | Admin      | 例外へ                         |
| ADM-002       | 予約管理        | Admin      | 検索/割当                      |
| ADM-003       | 顧客/機器       | Admin      | 閲覧/編集                      |
| ADM-004       | Partner/Area    | Admin      | 登録/停止/Zone                 |
| ADM-005       | 通知ポリシー    | Admin      | チャネル/費用                  |
| ADM-006       | 事故/監査       | Admin      | 例外処理                       |
| ADM-007       | KPI/Cost        | Admin      | 分析(P1)                       |
| CUS-008       | 担当変更/希望   | Customer   | 希望Partner変更/優先解除       |
| PAR-008       | 顧客関係表示    | Partner    | origin/preferred/serviceの確認 |
| ADM-008       | Compliance Case | Admin      | 申告/証拠/回答/措置            |

# 08 / UI/UX デザイン仕様

- HOMENECT承認ロゴの Navy / Teal を主軸にする。色値は実装前にブランドマスターから確定。

- Customerはインストール不要・スマホ縦持ちを基準。予約完了までの質問数を最小化。

- Partnerはスマホ縦持ち、片手操作。受付ON/OFF、受諾/辞退、HELPを1〜2タップで実行可能にする。

- PWAインストールを要求せず、通常Webでも同一機能を利用可能。

- LIFFは同一画面を表示するがService Worker/A2HSに依存しない。

- 破壊的操作は確認。色だけで状態を伝えない。WCAG相当のコントラスト/ラベルを確保。

# 09 / データ・ER 設計

| **Entity**           | **主要項目**                                                                                                  | **制約/目的**                        |
|----------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------|
| Customer             | id, name/contact, area, consent, preferred_partner_id                                                         | Core ID。LINE IDを主キーにしない     |
| ExternalIdentity     | subject_type/id, provider, provider_user_id, verified_at                                                      | LINE/email等を分離                   |
| Equipment            | customer_id, room, maker/model, type, notes, last_service_at                                                  | Customer 1:N                         |
| Partner              | legal_name, type, status, insurance/licenses, contract_version                                                | 個人/法人                            |
| PartnerUser          | partner_id, role, status                                                                                      | Owner/Admin/Technician               |
| AreaZone             | code, geometry/postal/municipality, active                                                                    | ルーティング単位                     |
| PartnerArea          | partner_id, zone_id, priority, skills, capacity                                                               | 独占権を意味しない                   |
| Reservation          | customer, equipment, partner, slot, price, status, source                                                     | Core transaction                     |
| JobOffer             | reservation, partner, terms_snapshot, expires_at, response                                                    | 条件明示証跡                         |
| WorkLog              | reservation, technician, before/after, start/end, abnormality                                                 | 品質                                 |
| HelpRequest          | reservation, requester, type, target, status                                                                  | Partner協働                          |
| CashReceipt          | reservation, amount, received_at, status                                                                      | P0                                   |
| Notification         | event, channel, cost_class, provider_result, idempotency_key                                                  | 再送/費用                            |
| CommunicationCost    | notification, units, estimated_cost, outcome                                                                  | P1                                   |
| Incident             | reservation, severity, category, summary, status                                                              | S1-S4                                |
| AuditEvent           | actor, action, entity, before/after, occurred_at                                                              | Append-only                          |
| CustomerRelationship | customer_id, source_type, origin_partner_id, preferred_partner_id, updated_reason                             | 顧客関係の継続性。所有権を意味しない |
| ComplianceCase       | id, customer_id, partner_id, reservation_id, allegation, evidence, partner_response, decision, action, status | 迂回取引等の事実確認/段階措置        |
| PIIAccessEvent       | actor, customer_id, reservation_id, field_scope, reason, occurred_at                                          | 連絡先/詳細住所等の閲覧監査          |

# 10 / API・外部連携仕様

| **Method** | **Endpoint**                          | **責務**                          | **Actor**        |
|------------|---------------------------------------|-----------------------------------|------------------|
| POST       | /api/reservations                     | 予約作成。Idempotency-Key必須     | Customer         |
| GET        | /api/availability                     | Zone/期間/サービスで空き          | Customer         |
| GET/PATCH  | /api/reservations/{id}                | 自分/権限内の予約                 | Customer/Admin   |
| POST       | /api/reservations/{id}/cancel         | 取消                              | Customer/Admin   |
| POST       | /api/identity/line/link               | LINE連携                          | Customer/Partner |
| POST       | /webhooks/line                        | 署名検証/イベント処理             | LINE             |
| GET        | /api/partner/offers                   | 案件オファー                      | Partner          |
| POST       | /api/partner/offers/{id}/accept       | 受諾                              | Partner          |
| POST       | /api/partner/offers/{id}/decline      | 辞退                              | Partner          |
| PUT        | /api/partner/availability             | 稼働/容量/Zone                    | Partner          |
| POST       | /api/worklogs                         | 作業報告                          | Technician       |
| POST       | /api/help                             | HELP起票                          | Partner          |
| POST       | /api/cash-receipts                    | 現金受領                          | Technician       |
| GET/POST   | /api/admin/\*                         | 管理・設定・監査                  | Admin            |
| POST       | /jobs/notifications                   | ポリシーに従いチャネル選択        | Scheduler        |
| POST       | /api/customers/{id}/preferred-partner | 顧客希望に基づく優先担当変更/解除 | Customer/Admin   |
| GET        | /api/partner/jobs/{id}/contact-scope  | 受諾状態に応じたPII開示範囲       | Partner          |
| POST       | /api/admin/compliance-cases           | 迂回取引等の申告/Case作成         | Admin            |
| PATCH      | /api/admin/compliance-cases/{id}      | 回答/証拠/判定/措置を記録         | Admin            |

- LINE Webhook は署名検証し、同一 event 再送で二重登録しない。

- LINE/Email/Push の結果を Notification に保存し、業務イベントと配信イベントを分離する。

- 案件オファー前は顧客住所/氏名等を必要最小限にマスクし、受諾後に権限を拡張する。

- すべての外部チャネルは Adapter 経由とし、COREから直接SDK依存を広げない。

# 11 / 非機能要件

| **ID** | **分類**           | **基準**                                                              |
|--------|--------------------|-----------------------------------------------------------------------|
| NFR-01 | Performance        | 通常API P95 1.5秒以内（画像除く）                                     |
| NFR-02 | UI                 | 主要Web画面の操作可能化 P95 3秒以内を目標                             |
| NFR-03 | Availability       | Pilot/商用 月99.5%以上目標                                            |
| NFR-04 | Capacity           | 初期100予約/日、Partner20社/施工者100名を劣化なく扱える設計           |
| NFR-05 | Image              | 元最大10MB/枚、保存時圧縮・容量監視                                   |
| NFR-06 | Backup             | RPO\<=24h / RTO\<=4hを初期目標                                        |
| NFR-07 | Browser            | iOS Safari/Chrome, Android Chrome 最新2世代、LINE内ブラウザは基本機能 |
| NFR-08 | PWA                | 外部ブラウザでInstallable。PWAなしでも主要機能可                      |
| NFR-09 | Maintainability    | 価格・手数料・通知ポリシーをConfig化                                  |
| NFR-10 | Cost observability | チャネル別送信量・推定変動費を集計可能                                |

# 12 / セキュリティ要件

| **ID** | **要件**                                                         |
|--------|------------------------------------------------------------------|
| SEC-01 | Customer/Partner/Adminの認証・認可を分離。Core IDを主とする。    |
| SEC-02 | Admin/Partner Ownerは商用前にMFA/強固な認証。                    |
| SEC-03 | DBはRLS等で自分/自社/割当案件のみに制限。                        |
| SEC-04 | 案件オファー段階のPIIを最小化し、受諾後に必要範囲だけ表示。      |
| SEC-05 | 画像Private、短期署名URL、Upload MIME/サイズ検証。               |
| SEC-06 | Secretsをコード/クライアントに埋め込まない。                     |
| SEC-07 | 料金・担当・状態・PII・権限・設定変更を監査。                    |
| SEC-08 | LINE token等はサーバー側で検証。クライアント申告IDを信用しない。 |
| SEC-09 | 通知誤送信/個人情報漏えいはS1/S2扱い。                           |

# 13 / テスト仕様

| **Test ID** | **Scenario**                    | **期待**                                                     |
|-------------|---------------------------------|--------------------------------------------------------------|
| TC-001      | Web新規予約→受諾→施工→現金→完了 | Pass                                                         |
| TC-002      | LINEなしで予約完了              | Pass                                                         |
| TC-003      | 任意LINE連携                    | Core ID維持/重複Customerなし                                 |
| TC-004      | Preferred Areaルーティング      | 正しい候補順                                                 |
| TC-005      | Preferred Partner休み→Backup    | Overflow成功                                                 |
| TC-006      | Partner辞退                     | 強制受託なし/次候補へ                                        |
| TC-007      | 案件提示条件                    | 報酬/日時/場所/作業内容等のsnapshot保存                      |
| TC-008      | HELP代行                        | 顧客優先担当は意図通り保持                                   |