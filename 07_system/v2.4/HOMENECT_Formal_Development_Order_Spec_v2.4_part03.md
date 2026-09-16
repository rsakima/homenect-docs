| TC-009      | 他Partner顧客アクセス           | 403/マスク                                                   |
| TC-010      | 画像権限                        | 署名URL期限/他者アクセス不可                                 |
| TC-011      | 予約競合                        | Capacity超過なし                                             |
| TC-012      | Webhook再送                     | 二重予約/通知なし                                            |
| TC-013      | 未成約ユーザーLINE Push         | ポリシーでBLOCK                                              |
| TC-014      | 重要通知Fallback                | Email/WebPush失敗→設定チャネル                               |
| TC-015      | LIFF内                          | Service Workerなしでも主要操作                               |
| TC-016      | PWA外部ブラウザ                 | Installable/通常Webとの整合                                  |
| TC-017      | 事故                            | Incidentへ遷移/通常完了不可                                  |
| TC-018      | Backup Restore                  | 主要テーブル整合                                             |
| TC-019      | 再予約(P1)                      | 同一Equipment再利用                                          |
| TC-020      | 通信費(P1)                      | NotificationとCost Ledger整合                                |
| TC-021      | HELP代行後の次回予約            | service_partnerが変わってもpreferred_partnerを自動変更しない |
| TC-022      | 顧客によるPartner変更希望       | 顧客意思でpreferred_partnerを変更/解除でき監査される         |
| TC-023      | 受諾前PII                       | 氏名/電話/詳細住所等が必要最小限にマスクされる               |
| TC-024      | 受諾後PII                       | 施工に必要な範囲だけ表示しアクセスを監査する                 |
| TC-025      | 迂回取引申告                    | Case作成→証拠→Partner回答→判定→措置を記録できる              |
| TC-026      | 誤申告/未立証                   | 申告だけで自動停止/契約解除されない                          |

# 14 / 受入基準

| **ID** | **合格条件**                                                                               |
|--------|--------------------------------------------------------------------------------------------|
| AC-01  | 顧客がLINEなしで予約可能                                                                   |
| AC-02  | 初回写真がPrivate保存され再試行可                                                          |
| AC-03  | 予約確定前に役務/価格/日時/支払/取消/契約主体を表示                                        |
| AC-04  | Partnerが受諾/辞退可能                                                                     |
| AC-05  | Preferred Area/Backupで複数Partner運用可能                                                 |
| AC-06  | 案件提示条件が記録される                                                                   |
| AC-07  | Before/After/異常/試運転を保存                                                             |
| AC-08  | 現金受領が案件と紐づく                                                                     |
| AC-09  | HELPで代行/応援が処理できる                                                                |
| AC-10  | 他Customer/他Partnerデータを閲覧不可                                                       |
| AC-11  | 未成約への課金LINE Pushを原則BLOCK                                                         |
| AC-12  | LINE障害でもWeb主要フローが継続                                                            |
| AC-13  | 監査ログ確認可能                                                                           |
| AC-14  | Backup復元Pass                                                                             |
| AC-15  | S1/S2=0                                                                                    |
| AC-16  | 環境/運用/障害/設定/法務Open Gate一覧を納品                                                |
| AC-17  | origin/preferred/service partnerを分離して保持し、HELP施工だけで優先担当が自動変更されない |
| AC-18  | 顧客が希望する場合は優先担当を変更/解除できる                                              |
| AC-19  | 受諾前PIIを最小化し、受諾後の閲覧を監査できる                                              |
| AC-20  | Compliance Caseで申告・証拠・Partner回答・判定・段階措置を記録できる                       |

# 15 / インフラ・環境構成

- Dev / Staging / Production を分離し、実データとSecretsを混ぜない。

- Git + Pull Request、DB migration、Rollback 手順を必須とする。

- Supabase を参照構成とし、Web/PWAホスティングはCloudflare/Vercel等を比較可能。

- Email/Web Push/LINEは環境別にProvider設定を分離する。

- 本番ドメイン・送信ドメイン・LINE Channelは環境変数化する。

# 16 / 運用・保守設計

| **契機** | **確認**                        | **対応**                     |
|----------|---------------------------------|------------------------------|
| 毎朝     | 予約、未受諾、Partner休み、HELP | 例外だけ再割当/連絡          |
| 日中     | 事故、変更、取消、問い合わせ    | Severityで例外対応           |
| 夕方     | 未完了、写真、現金記録          | 不足を当日確認               |
| 週次     | 未精算、KPI、Backup、通知費     | 異常値確認                   |
| 月次     | LINE/Email/Push使用量と料金     | プラン/ポリシー最適化        |
| 障害     | Channel/API/DB                  | Core保護→Fallback→復旧後追記 |

# 17 / スケジュール・タスク

| **Milestone**      | **成果物**                                  | **Exit**        |
|--------------------|---------------------------------------------|-----------------|
| M0 要件ロック      | v2.0仕様差分、法務Open Gate、WBS            | Blocker 0       |
| M1 Core/Identity   | Web、DB、Auth/RLS、Storage、Channel Adapter | 認証/権限Pass   |
| M2 Booking/Partner | 予約、Area、JobOffer、WorkLog、Cash         | 単体/結合Pass   |
| M3 Network         | Backup/HELP/Notification Policy             | 複数Partner E2E |
| M4 E2E/修正        | 権限/性能/障害/復元                         | S1/S2=0         |
| M5 引渡し          | Staging/Prod、運用資料                      | AC-01〜16 Pass  |
| Option P1          | PWA Push、Repeat、Cost Ledger、KPI          | P1検収          |

# 18 / リスク・課題管理

| **Risk**                          | **Severity** | **Mitigation**                                                                |
|-----------------------------------|--------------|-------------------------------------------------------------------------------|
| 薄利/料金未確定                   | High         | Config化、Pilotで獲得元別採算                                                 |
| Partner供給不足                   | High         | Capacity、Backup、HELP                                                        |
| 顧客/エリア分割と誤解されるルール | High         | 独占禁止、Preferred Area限定、法務Gate                                        |
| フリーランス取引条件不備          | High         | JobOffer Terms Snapshot                                                       |
| 個人情報のPartner間漏えい         | High         | PIIマスク、RLS、監査                                                          |
| 事故/水漏れ                       | High         | 前後記録、Incident、保険Gate                                                  |
| LINE料金/仕様変更                 | Medium       | Web First、Adapter、Cost Policy                                               |
| Web Push許可/端末差               | Medium       | Email/LINE Fallback、Push非必須                                               |
| LIFF制約                          | Medium       | PWA機能をLIFF内に依存させない                                                 |
| 要求膨張                          | Medium       | P0/P1/P2とCR                                                                  |
| 施工者による顧客引き抜き/迂回取引 | High         | Relationship source、PII段階開示、低リピート摩擦、監査、契約、Compliance Case |
| 過度な引き抜き禁止/顧客囲い込み   | High         | HOMENECT由来接点に限定、顧客選択権、法務Gate、独占/相互不可侵を禁止           |
| 誤申告によるPartner不利益         | Medium       | 申告のみで自動処分せず、証拠/回答/人間判断/段階措置                           |

# 19 / 仕様変更履歴

| **CR** | **Date**   | **変更**                                                                            | **Decision** | **Version** |
|--------|------------|-------------------------------------------------------------------------------------|--------------|-------------|
| CR-000 | 2026-09-15 | 旧正式開発発注仕様書 v1.0 作成                                                      | Approved     | v1.0        |
| CR-001 | 2026-09-16 | ブランドをHOMENECTへ統合、沖縄先行・全国展開                                        | Approved     | v2.0        |
| CR-002 | 2026-09-16 | LINE FirstをWeb First / PWA Optional / LINE Connectedへ変更                         | Approved     | v2.0        |
| CR-003 | 2026-09-16 | Preferred Area / Backup / HELP / 優先担当を追加                                     | Approved     | v2.0        |
| CR-004 | 2026-09-16 | Cost-aware Notification / 未成約LINE Push原則禁止                                   | Approved     | v2.0        |
| CR-005 | 2026-09-16 | Relationship Protection / Anti-Circumvention / staged PII / Compliance CaseをP0追加 | Approved     | v2.1        |

# 20 / Decision Log

| **ID** | **Topic**                  | **Status**          | **Decision**                                                     |
|--------|----------------------------|---------------------|------------------------------------------------------------------|
| D-001  | Web First                  | Adopted             | CustomerはWebを標準。LINE必須にしない。                          |
| D-002  | Partner PWA                | Adopted as optional | 高頻度Partnerに推奨。通常Webでも利用可。                         |
| D-003  | LINE Connected             | Adopted             | 問い合わせ/任意連携/重要通知。                                   |
| D-004  | Native App                 | Deferred            | MVPでは作らない。                                                |
| D-005  | Paid LINE to leads         | Rejected by default | 未成約は原則0。                                                  |
| D-006  | Preferred Area             | Adopted             | HOMENECT案件の優先配信。独占ではない。                           |
| D-007  | Preferred Partner          | Adopted             | 顧客継続性用。所有権を意味しない。                               |
| D-008  | Backup/HELP                | Adopted             | Partner協働をP0化。                                              |
| D-009  | Fixed 20% fee              | Rejected            | 獲得元・価値・採算で決定。                                       |
| D-010  | MVP cash                   | Adopted             | 顧客→Partner直接。                                               |
| D-011  | Supabase                   | Reference           | 同等以上の代替可。                                               |
| D-012  | Business KPI as acceptance | Rejected            | システム検収と事業実証を分離。                                   |
| D-013  | Relationship Protection    | Adopted             | origin/preferred/service partnerを分離。HELP後の自動移管を防止。 |
| D-014  | Anti-Circumvention         | Adopted             | HOMENECT由来顧客への迂回勧誘を禁止対象とする。                   |
| D-015  | Customer Choice            | Adopted             | 顧客のPartner変更意思を優先する。                                |
| D-016  | Violation Due Process      | Adopted             | 申告→証拠→回答→人間判断→段階措置。自動罰金/即解除なし。          |

# 21 / 本番/Pilot 前 Gate

| **Gate** | **条件**                                                           |
|----------|--------------------------------------------------------------------|
| G-01     | 本番価格/Partner報酬/利用料を確定                                  |
| G-02     | 施工契約主体/表示/規約を確定                                       |
| G-03     | Preferred Area・顧客優先担当・価格/応援ルールの法務レビュー        |
| G-04     | Partner保険/資格の実在確認                                         |
| G-05     | フリーランス法対象案件の取引条件明示を実装/確認                    |
| G-06     | キャンセルポリシー確定                                             |
| G-07     | Backup Partnerを実在確認しE2E                                      |
| G-08     | Privacy/Terms/Partner Data Accessをレビュー                        |
| G-09     | LINE/Email/WebPush料金上限・ポリシーを設定                         |
| G-10     | Backup/Restore/Monitoringを実地確認                                |
| G-11     | HOMENECT商標/ドメイン/ブランド資産を最終確認                       |
| G-12     | 迂回取引防止条項の対象・期間・措置・違約条項を法務レビュー         |
| G-13     | リピート利用料/HELP案件報酬が直接迂回を過度に誘発しないかPilot検証 |

# 22 / 公式参照先

- https://developers.line.biz/ja/docs/messaging-api/pricing/

- https://www.lycbiz.com/jp/news/line-official-account/20260216/

- https://developers.line.biz/ja/docs/liff/differences-between-liff-browser-and-external-browser/

- https://www.jftc.go.jp/dk/guideline/unyoukijun/jigyoshadantai.html

- https://www.jftc.go.jp/freelancelaw_2025/

v2.1 追加決定（2026-09-16）：Relationship Protection / Anti-Circumvention をP0へ追加。

# 26. Price Protection / HELP Pricing Addendum

2026-09-16正式採用。以下は既存P0要件へ追加し、実装・試験・検収対象とする。

- P0：Reservationにcustomer_price_locked、handoff_typeを保持する。

- P0：HELP成立時にsupport_payout、platform_fee、必要に応じsupport_subsidyを保存する。

- P0：HELPではcustomer_price_lockedを原則維持し、service_partnerのみ変更可能とする。

- P0：Referralでは新しいprice snapshotとcustomer approvalを取得後に確定する。

- P0：追加作業はadditional_work_approved_atと金額・内容の承認履歴を必須とする。

- P0：応援案件のmarginが設定閾値未満の場合はauto-acceptを禁止し、Admin Exceptionへ送る。

- P0：Partner間の通常販売価格を相互開示するUIを作らない。案件提示では必要な受託条件のみ表示する。

- P0：契約主体、料金受領者、service_partner、warranty/incident ownerを案件ごとに再現可能にする。