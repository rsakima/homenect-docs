# HOMENECT 事業構想マスター

> **同期元:** `15_開発会社向け正式資料/HOMENECT_Business_Concept_Master_v2.2.docx` / 2026-09-16 完成版

> Business Concept Master v2.2 / 2026-09-16

> 正式ブランド、事業、ネットワーク、チャネル、開発判断の統合正本

> FORMAL MASTER

## 0. この文書の位置づけ

本書は、2026-09-15時点の正式原本「Okinawa HomeCare Network Business Concept Master v2.0」を事業原点として維持しつつ、その後に正式採用されたHOMENECTブランド、全国展開前提、Web First / PWA Optional / LINE Connected、Preferred Area、Backup / HELP、顧客関係保護・迂回取引防止を統合した正式事業構想マスターです。

本書で「正式採用」とした項目は、以後の分かりやすい説明資料、開発発注仕様、契約・運用資料へ展開します。ただし、料金、報酬、契約主体、キャンセル条件、保険・資格の実在、法的条項等の未確定事項は推測で埋めず、Gateまたは別紙で確定します。

### 正本の優先順位

1. 事業・運用判断：本書（Business Concept Master v2.2）
2. 開発実装・検収：Formal Development Order Spec v2.1 / Requirements Traceability v2.1
3. 数値・運用台帳：Business Operations Master v2.2
4. 人向け説明：Easy Overview、1枚資料、Partner募集資料等
5. 契約：正式締結版の利用規約・Partner契約・個別案件条件書（本書より優先）

## 1. Executive Summary

HOMENECTは、家のことで困っているお客様と、地域で仕事をする独立事業者・法人をつなぐHomeCare Networkです。沖縄でエアコンクリーニングから開始し、顧客獲得、予約、施工記録、再注文、地域内の助け合いを一つにつなぎ、実証後に住宅清掃、修理、水回り、電気等へ拡張し、将来は全国展開を目指します。

顧客向けはインストール不要のWebを基本とし、LINEは問い合わせ・任意連携・重要通知等の補助チャネルとして利用します。協力業者はWeb/PWAを主要業務UIとし、受付ON/OFF、案件確認、受諾/辞退、作業報告、応援依頼等を行います。HOMENECT COREが顧客、機器、協力業者、Area、予約、案件提示、施工記録、通知、監査等を一元管理し、LINE等の特定チャネルへ業務ロジックを依存させません。

協力業者間の顧客争奪を抑えながら助け合えるよう、Preferred Area、preferred_partner、Backup、HELP、Relationship Protectionを採用します。ただし顧客を「所有」せず、顧客本人の選択権を優先し、エリアを他社の営業禁止地域にはしません。

### 正式方針サマリー

| 論点 | 正式方針 | 状態 |
| --- | --- | --- |
| Brand | HOMENECT | Adopted |
| Start Category | エアコンクリーニング | Adopted |
| Start Region | 沖縄 | Adopted |
| Expansion | 全国展開前提 | Adopted |
| Customer UX | Web First | Adopted |
| Customer LINE | Optional / Connected | Adopted |
| Partner UX | Web / PWA | Adopted |
| LINE | Connected Channel | Adopted |
| Native App | MVPでは作らない | Deferred |
| Preferred Area | HOMENECT案件の優先ルーティング | Adopted |
| Backup / HELP | 地域Partnerの助け合い | Adopted |
| Customer Relationship | 起点・優先担当・実施工を分離 | Adopted |
| Anti-Circumvention | HOMENECT由来顧客の不正迂回を防止 | Adopted |
| Customer Choice | 顧客本人の担当変更権を維持 | Adopted |
| Payment | MVPは顧客→Partner現金直接 | Adopted |
| Fixed 20% | 採用しない | Rejected |
| Paid LINE Push to Leads | 原則行わない | Rejected by default |

## 2. 事業の原点（v2.0から維持）

### 2.1 Vision

エアコンクリーニングを入口に、地域の独立事業者が顧客獲得、予約、施工、写真記録、再注文、繁忙時の助け合いを無理なく行える仕組みを作ります。沖縄で小さく実証し、事業性・品質・供給が成立した後に、複数Partner・複数HomeCareカテゴリへ広げます。

### 2.2 最初から固定しないもの

- 本番価格。
- Partner報酬。
- HOMENECT利用料・手数料。
- 1日あたり固定訪問件数。
- 契約主体の細部。
- キャンセル・保証・再施工・返金条件。
- 未実在Partner・保険・資格。

### 2.3 最初から維持する原則

- エアコンクリーニングから開始。
- 顧客・施工者が簡単に使えること。
- 初回は必要情報を記録し、再注文で再入力を減らす。
- 一律20%手数料にしない。
- 施工者の既存顧客を強制的にHOMENECTへ移さない。
- Pilot前の価格・報酬・能力値は仮説として扱う。
- 事業実証前に全国・多カテゴリを同時展開しない。

## 3. Stakeholders

### 3.1 Customer

住宅・店舗等のHomeCareサービスを依頼する利用者。初期はエアコンクリーニングを利用します。

### 3.2 Partner

個人事業者または法人として独立してエアコンクリーニング等を提供する事業者。案件単位で受諾・辞退を選択します。

### 3.3 Partner User / Technician

Partnerに所属または紐づき、現場作業・作業報告を行う担当者。

### 3.4 HOMENECT Admin

顧客、予約、Partner、Area、通知、事故、監査、設定等を運用するHOMENECT運営者。

### 3.5 Backup / Specialist Partner

満席・休業・辞退時の応援、難機種、将来の専門カテゴリ等を担当するPartner。

## 4. 提供価値

### Customer

- Webから簡単に料金・空き確認・予約。
- 専用アプリ不要。
- 機器・施工履歴を残す。
- 次回は前回データを再利用。
- 担当Partnerが満席でもBackupへつなげる。
- 顧客本人が担当変更を希望できる。

### Partner

- HOMENECT獲得案件を受けられる。
- 受付ON/OFF、Capacity、対応エリアを自分で設定。
- 案件ごとに受諾・辞退。
- 作業記録・写真を整理。
- 忙しい・休み・難機種等はHELPを使える。
- 自力獲得顧客を一律に取り上げられない。
- 独立事業者として参加。

### HOMENECT

- 顧客獲得と需要集約。
- 品質・作業記録の標準化。
- Areaベースの供給調整。
- Partner Networkの構築。
- 再注文・紹介・地域拡張。
- 将来HomeCare OSへ拡張可能なCore構造。

## 5. Service Scope

### MVP / P0

- エアコンクリーニング。
- Customer Web予約。
- Partner Web案件管理。
- Admin Web管理。
- Customer / Equipment。
- 写真アップロード。
- 空き枠・料金表示。
- Reservation lifecycle。
- Partner onboarding / availability / skills / area。
- Preferred Area routing。
- preferred_partner continuity。
- JobOffer / Terms Snapshot。
- Accept / Decline / Expiry。
- Backup / Overflow。
- WorkLog / Before / After / 異常 / 試運転。
- CashReceipt。
- HELP。
- Notification Policy / LINE adapter / Email adapter。
- Auth / RLS / Audit / Backup / Fallback。
- Relationship Protection / Anti-Circumvention / staged PII / Compliance Case。

### P1

- 「前回と同じ」再注文。
- 6/12か月等の再注文通知。
- PWA installability / Web Push。
- Communication Cost Ledger。
- KPI Dashboard。
- 精算・売上表示の強化。

### Later

- オンライン決済。
- 他HomeCareカテゴリ。
- Specialist資格・カテゴリ別routing。
- 全国展開機能強化。
- AI最適化等は実証後に判断。

## 6. Channel Architecture

### Architecture Decision

**Web First / PWA Optional / LINE Connected / Channel Independent Core**

### Customer

- Responsive Webを標準UI。
- LINEアカウントなしでも料金確認・予約可能。
- LINEは問い合わせ、任意identity link、重要通知等。
- LIFFはLINEから同じWebを開く入口として利用。
- Customer PWA installは必須にしない。

### Partner

- Responsive Webを標準UI。
- 高頻度利用Partnerは外部ブラウザからPWA install可能。
- Web Pushを利用可能な場合は低コスト通知に利用。
- LINEは補助通知・問い合わせ・緊急時等。
- LIFF内のService Worker / Add to Home Screenに依存しない。

### Admin

- Web Dashboard。
- 顧客・予約・Partner・Area・Notification Policy・Incident・Audit・KPI等。

### HOMENECT CORE

Customer、Equipment、Partner、AreaZone、Reservation、JobOffer、WorkLog、HelpRequest、Notification、Audit等の業務データ・業務ロジックをCoreへ集約し、LINE userId等をCoreの主キーにしません。

## 7. Customer Journey

1. 広告・SEO・SNS・紹介・Partner経由等からWebへ流入。
2. サービス・料金・対応範囲を確認。
3. 初回はエアコン情報・必要写真を登録。
4. 空き枠・料金を確認。
5. 予約最終確認で役務、数量、料金、支払、キャンセル、契約主体等を確認。
6. Reservation作成。
7. 希望者はLINE連携。
8. Area / skills / preferred Partner / capacityによりJobOffer。
9. Partner受諾。
10. 施工。
11. Before / After / 異常 / 試運転 / Cash receiptを記録。
12. 完了。
13. P1で再注文、Reminder。

## 8. Partner Journey

1. Onboarding。
2. 保険・資格・技能・Area・Capacity登録。
3. 受付ON/OFF。
4. JobOfferを確認。
5. 案件条件を見て受諾/辞退。
6. 受諾後に必要なPIIを確認。
7. 施工。
8. WorkLog。
9. CashReceipt。
10. 必要時HELP。
11. Completed。
12. 将来売上・精算を確認。

## 9. Partner Network

### Preferred Area

PartnerごとにAreaZoneを設定し、HOMENECT由来案件の優先候補として利用します。これは排他的営業区域ではありません。

### Backup / Overflow

第一候補が満席、OFF、辞退、期限切れ等の場合に次候補へ提示します。

### HELP

- 忙しい。
- 休み・体調不良。
- 難機種。
- 技術相談。
- 事故対応。
- その他運用支援。

### Partner autonomy

案件単位で受諾・辞退できる状態を維持します。固定勤務、強い指揮命令等をシステムで作ることを目的にしません。

## 10. Relationship Protection / Anti-Circumvention

### 10.1 顧客を所有しない

Customerの法的・経済的所有権をPartnerへ設定する設計は採用しません。

### 10.2 Relationship source

顧客の関係を区別して記録します。

- homenect_acquired。
- partner_acquired。
- help等。

### 10.3 Origin / Preferred / Service Partner

- `origin_partner_id`：顧客関係の起点。
- `preferred_partner_id`：次回優先提示先。
- `service_partner_id`：今回実際に施工したPartner。

HELPでB社が施工しても、A社のpreferred関係を自動でB社へ移しません。

### 10.4 Customer Choice

顧客本人がB社等への変更を希望した場合は、本人意思を確認したうえでpreferredを変更・解除可能にします。

### 10.5 Anti-Circumvention

HOMENECTを通じて取得した顧客情報を利用して、HOMENECTを介さず直接契約・直接予約へ不正に誘導する行為を契約上の禁止対象とします。

対象をPartnerの全顧客・全営業活動へ広げず、HOMENECT由来接点の保護に限定します。期間、違約金・措置等はG-12で法務確認します。

### 10.6 Staged PII Disclosure

JobOffer提示時は、Area、概算場所、作業内容、日時、報酬等を中心に提示し、Customerの氏名、電話、詳細住所等のPIIを最小化します。Accept後に必要範囲を開示します。

### 10.7 Compliance Case

引き抜き等の申告があった場合、次の流れで記録します。

1. allegation。
2. evidence / logs。
3. Partner response。
4. operator decision。
5. warning / distribution pause / qualification pause / termination等。

顧客申告1件のみで重大処分を自動実行しません。ただし緊急安全措置は別です。

## 11. Area Routing

推奨順序：

1. Customer / ReservationのAreaZoneを解決。
2. preferred_partner_id確認。
3. service / equipmentに必要なskills / qualification / insurance確認。
4. Preferred Area候補。
5. Partner availability / capacity / status確認。
6. JobOffer。
7. decline / expiry / no capacityの場合Backup。
8. 必要時Network Open。

ルーティング条件・優先順位・重みはConfig化し、コードへ固定しすぎません。

## 12. Reservation / JobOffer

### Reservation

顧客の予約取引Core。

最低限：

- customer_id。
- equipment_id。
- requested slot。
- service / quantity。
- displayed price snapshot。
- status。
- acquisition source。
- assigned/service partner。
- cancellation / completion metadata。

### JobOffer

Partnerへ1件の仕事を提示した証跡。

最低限：

- reservation_id。
- partner_id。
- terms_snapshot。
- presented_at。
- expires_at。
- accepted / declined / expired。
- response_at。

Partnerへ提示した作業内容、日時、場所、報酬、支払条件等を後から再現できる状態にします。

## 13. Customer / Equipment

### Customer

Core customer_idを持ち、LINE userId / email等を直接主キーにしません。

### ExternalIdentity

- subject_type / subject_id。
- provider。
- provider_user_id。
- verified_at。

同じCustomerへ複数チャネルをlinkできる設計にします。

### Equipment

- customer_id。
- room。
- maker / model。
- type。
- photos。
- notes。
- last_service_at。

再注文時は同一equipmentを再利用可能にします。

## 14. Data Model

主要Entity：

- Customer。
- ExternalIdentity。
- Equipment。
- Partner。
- PartnerUser。
- AreaZone。
- PartnerArea。
- Reservation。
- JobOffer。
- WorkLog。
- HelpRequest。
- CashReceipt。
- Notification。
- CommunicationCost。
- CustomerRelationship。
- ComplianceCase。
- PIIAccessEvent。
- Incident。
- AuditEvent。

## 15. Notification / Communication Cost

### Notification Engine

イベント発生時に、重要度、状態、チャネル接続、到達性、費用、顧客設定等を見て配信チャネルを選びます。

### 初期優先

1. Web / in-app。
2. Email。
3. Web Push（利用可能時）。
4. LINE Push（必要な高価値場面）。

### Paid LINE to Unconverted Leads

未成約Customer / Leadへの課金対象LINE Pushは原則BLOCKします。

### Communication Cost Ledger

P1でNotificationごとのchannel、billing unit、estimated cost、outcomeを記録し、Customer数ではなく必要な取引×必要な通信に費用が比例する状態を目指します。

## 16. Payment / Revenue

### MVP Payment

Customer → Partnerへ現金直接支払を基本とします。

PartnerはCashReceiptを登録します。

### HOMENECT Revenue

一律20%を採用しません。

候補：

- HOMENECT新規獲得案件：獲得・提供価値を反映した利用料。
- Partner self-acquired：低い固定/利用料等の候補。
- Repeat：初回より低い利用料等を検証。
- HELP：応援報酬・利用条件を明示。

確定条件ではなくG-01 / Pilotでunit economicsを確認して決定します。

### Unit Economics

`1訪問限界利益 = Customer revenue - Partner payout - other variable cost - Cash CAC - communication variable cost`

Acquisition source別に管理します。

## 17. Pricing / Capacity

### Pricing

旧ヒアリング価格・参考価格は本番料金として固定しません。

### Capacity

1日6件等を固定しません。

Partnerが：

- daily capacity。
- time slots。
- holiday / blackout。
- service skills。
- accepting ON/OFF。

を設定します。

インタビューで1日5件程度等の情報がある場合も参考値として扱います。

## 18. WorkLog / Quality

最低限：

- technician。
- started_at / completed_at。
- Before photos。
- After photos。
- abnormality。
- test operation。
- comments。
- customer explanation。

異常時はnormal completionではなくIncident等へ分岐可能にします。

## 19. Incident / Safety

事故・品質問題を通常案件と分離して記録します。

候補severity：

- S1：人身・重大漏水・重大privacy等。
- S2：重大な物損・サービス継続影響等。
- S3：軽微な再施工・クレーム等。
- S4：情報・運用レベル。

Severity定義は正式Operationsで確定します。

## 20. Admin Operations

日常運用はHuman on Exceptionを基本とします。

### Morning

- Today's reservations。
- unassigned / unanswered offers。
- Partner availability。
- HELP / incidents。

### Daytime

- changes / cancellations。
- inquiry。
- HELP。
- incident。

### Evening

- incomplete jobs。
- missing photos。
- missing cash record。
- next day exceptions。

### Weekly / Monthly

- sales / contribution margin。
- acquisition source。
- Partner acceptance / capacity。
- complaints / rework。
- notification cost。
- backup / restore。

## 21. Security / Privacy

- Customer / Partner / Admin authentication。
- Role / RLS等によるtenant・assignment boundary。
- Private image storage。
- short-lived signed URL等。
- token / webhook server-side verification。
- secretsをclientへ露出しない。
- price / assignment / status / PII / permission / configurationのaudit。
- PII staged disclosure。
- PII access log。
- backup / restore。

詳細はDev Spec v2.1を正とします。

## 22. Reference Architecture

現時点のReference Architecture：

- Frontend：Responsive Web / PWA。
- Customer LINE：LINE Official Account / LIFF optional。
- Backend：Supabase PostgreSQL / Auth / Storage / Edge Functions等を標準候補。
- Notifications：LINE adapter / Email adapter / Web Push adapter。
- Admin：Web Dashboard。

ただし開発会社が同等以上の代替構成を提案することを禁止しません。Security、cost、operation、migration、vendor lock-in等の比較理由を求めます。

## 23. NFR方針

- Major API P95：初期1.5秒以内目標（画像除外）。
- Customer / Partner Web：主要操作P95 3秒以内目標。
- Pilot / commercial availability：99.5%以上目標。
- Pilot initial capacity：100 reservations/day、Partner20社、Technician100名を目安に設計し、実測に応じて更新。
- image upload：最大10MB/枚程度を初期上限候補、保存時最適化。
- RPO：24h以内初期目標。
- RTO：4h以内初期目標。
- iOS Safari / Chrome、Android Chrome等主要ブラウザ。
- LINE内は主要Web操作ができ、PWA機能依存を避ける。

最終NFRはDev Specを正とします。

## 24. Acquisition / Attribution

Reservationまたはacquisition touchpointに次を保持できる構造：

- organic / SEO。
- paid ads。
- Partner QR / NFC / referral。
- customer referral。
- SNS。
- LINE。
- direct / unknown。

「LINE追加数」だけをsuccess KPIにせず、sourceごとにreservation、Cash CAC、contribution margin、repeatを追跡します。

## 25. Reviews / Referral

施工後にreview / referralを依頼できますが、満足度の回答により「高評価者だけGoogle Reviewへ誘導、低評価者だけ内部へ送る」等のreview gatingは採用しません。

内部フィードバック導線は公開review導線と別に全顧客へ提供可能です。

## 26. Pilot

Pilotは事業実証です。

確認：

- reservation completion rate。
- Customer complaints / rating / referral。
- repeat（期間が許す範囲）。
- Partner acceptance / decline。
- Partner time economics。
- Area supply / overflow success。
- per-visit contribution margin by source。
- communication variable cost。
- worklog completion。
- incident / rework。

少数sampleでKPI未達を即事業失敗判定しないよう、System acceptanceとBusiness hypothesis evaluationを分離します。

## 27. Expansion

順序：

1. complete service / system。
2. internal E2E。
3. Okinawa limited Pilot。
4. validate quality / supply / economics。
5. expand Okinawa density。
6. one external region。
7. nationwide region-by-region。

新カテゴリは既存カテゴリの品質・利益・運用が安定してから追加します。

## 28. Competition / Network Guardrails

- Preferred Areaは他社営業禁止にしない。
- Partner同士で一般販売価格を共同固定しない。
- Customerを所有物扱いしない。
- 案件受諾を強制しない。
- HELPをCustomer theft mechanismにしない。
- Partner自力顧客を一律強制移管しない。
- Anti-CircumventionはHOMENECT由来情報・接点へ限定。
- 顧客本人の選択を優先。
- 競争法上の妥当性をG-03 / G-12で専門家確認。

## 29. Freelance / Partner Transaction Guardrails

Partnerが法令上のフリーランス等に該当する場合を想定し、案件提示時に：

- work content。
- date / place。
- compensation。
- payment terms / due date。
- other required conditions。

等を電磁的方法で提示・保存できるJobOffer Terms Snapshotを設計します。

HOMENECTは労働者性の最終法的評価を本書だけで断定しません。案件辞退自由、availability自己設定等を維持しつつ、実態を契約・運用と一致させる必要があります。

## 30. Decision Log

| ID | Decision | Status |
| --- | --- | --- |
| D-001 | HOMENECT | Adopted |
| D-002 | Customer Web First | Adopted |
| D-003 | Partner PWA | Adopted optional |
| D-004 | LINE Connected | Adopted |
| D-005 | Native App MVP | Deferred |
| D-006 | Paid LINE to leads | Rejected by default |
| D-007 | Preferred Area | Adopted |
| D-008 | Preferred Partner | Adopted |
| D-009 | Backup / HELP | Adopted |
| D-010 | Fixed 20% fee | Rejected |
| D-011 | MVP cash | Adopted |
| D-012 | Review gating | Rejected |
| D-013 | Relationship Protection | Adopted |
| D-014 | Anti-Circumvention | Adopted |
| D-015 | Customer Choice | Adopted |
| D-016 | Violation Due Process | Adopted |

## 31. Risk Register

### High

- R-01：price / margin not validated。
- R-02：Partner supply shortage。
- R-03：Area/customer rule competition law risk。
- R-04：freelance transaction condition defect。
- R-05：cross-Partner PII leakage。
- R-06：water / damage incident。
- R-10：Partner customer poaching / circumvention。
- R-11：overbroad non-solicit / customer enclosure。

### Medium

- R-07：LINE pricing / specification change。
- R-08：Web Push permission / browser difference。
- R-09：LIFF limitation。
- R-12：false allegation against Partner。

## 32. Launch / Legal Gates

| Gate | Condition |
| --- | --- |
| G-01 | Production price / Partner payout / fee confirmed |
| G-02 | Service contract party / legal display / terms confirmed |
| G-03 | Preferred Area / customer relationship / competition-law review |
| G-04 | Partner insurance / qualification existence verified |
| G-05 | Freelance Act transaction condition handling confirmed |
| G-06 | Cancellation policy confirmed |
| G-07 | Backup Partner actually available and E2E tested |
| G-08 | Privacy / Terms / Partner data access reviewed |
| G-09 | LINE / Email / Web Push cost limits and policy confirmed |
| G-10 | Backup / restore / monitoring tested |
| G-11 | HOMENECT trademark / domain / brand assets checked before public release |
| G-12 | Anti-circumvention scope / duration / sanction / liquidated damages legal review |
| G-13 | Repeat fee / HELP economics does not create excessive circumvention incentive; Pilot validation |

## 33. Completion Definition

Business Conceptが「完成」と言える条件：

- major stakeholders defined。
- Customer / Partner / Admin flows defined。
- P0 / P1 scope defined。
- Channel strategy defined。
- Partner Network defined。
- Relationship Protection defined。
- Revenue principle defined without invented production numbers。
- legal / price / operational unknowns converted to explicit Gates。
- development requirements traceable。
- Pilot measurement separated from software acceptance。

上記を満たしたため、本書は**事業構想マスター v2.2**として正式採用します。
