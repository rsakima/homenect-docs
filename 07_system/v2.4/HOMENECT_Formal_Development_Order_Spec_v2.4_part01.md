**HOMENECT**

**正式開発発注仕様書**

Formal Development Order Specification

Development Order Spec v2.4

基準日：2026-09-16  
CONFIDENTIAL / FORMAL MASTER

| 正式版の基準：旧正式マスター v2.0 を出典とし、2026-09-16 までに承認した HOMENECT ブランド、沖縄先行・全国展開、Web First / PWA Optional / LINE Connected、Partner Network、低変動通信費設計を反映。過去に生成された v3.0 系資料は正本として使用しない。 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>本書の位置づけ<br />
HOMENECT Business Concept Master v2.3 を上位の事業正本とし、本書を見積・設計・実装・テスト・検収の最上位実装正本とする。矛盾時は「最新の承認済 Decision Log → 本書 → Business Concept Master v2.3 → 過去資料」の順。</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **項目**                | **内容**                                                                                                          |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| 発注対象                | HOMENECT Web Platform / Partner Network                                                                           |
| 初期商材                | エアコンクリーニング                                                                                              |
| 主要UI                  | Customer: Web / optional LIFF, Partner: Web/PWA, Admin: Web                                                       |
| チャネル                | LINE / Email / Web Push を Adapter として接続                                                                     |
| 発注方式                | P0 基本 + P1 オプション分離見積。P2以降は別CR。                                                                   |
| 基準日                  | 2026-09-16                                                                                                        |
| Relationship Protection | Customer source / origin/preferred/service partner / staged PII / anti-circumvention / compliance case をP0に含む |


# 00 / v2.4 実装ロック（2026-09-16）

本版で、P0実装開始に必要な技術・状態・データ・API・画面・運用の基準をロックする。開発者は、未確定の事業実数値を除き、下記を独自判断で変更しない。

| 項目 | 正式採用 | 補足 |
|---|---|---|
| Web Framework | **Next.js + TypeScript** | App Router。Customer/Partner/Adminを同一モノレポで管理 |
| Runtime | **Node.js LTS** | 正確なpatchは初回lockfileで固定 |
| Package Manager | **pnpm** | lockfileをコミット |
| UI | **Responsive Web / Tailwind CSS + design tokens** | Customer/PartnerはMobile First、AdminはDesktop First |
| Database | **Supabase PostgreSQL** | migrationを唯一のschema変更手段とする |
| Authentication | **Supabase Auth** | Core SubjectとExternalIdentityを分離 |
| Authorization | **PostgreSQL RLS + server-side RBAC** | 二重防御。Admin例外操作はreason + audit必須 |
| Storage | **Supabase Storage Private Bucket** | 公開URL禁止、短期signed URL |
| Server/API | **Next.js Server API + Supabase Edge Functions（外部Webhook/worker）** | 業務ルールはUse Case層に集約 |
| Background | **Transactional Outbox + scheduled worker** | 通知、offer expiry、retryをDBと一貫処理 |
| LINE | **Messaging API + LIFF Adapter** | LINEをCore IDや唯一UIにしない |
| Email | **Provider Adapter** | Provider交換可能 |
| Web Push | **P1** | Partner中心。P0は必須にしない |
| Test | **Vitest + Playwright + SQL/RLS tests** | P0はE2E受入まで自動化 |
| CI/CD | **GitHub Actions** | lint/typecheck/test/build/migration check |
| Monitoring | **Structured logs + Sentry等のError Tracking** | Providerログも併用 |
| Deployment | **Next.js managed hosting + Supabase** | P0参照構成。独自基盤へ変更はCR |

![HOMENECT Architecture](diagrams/HOMENECT_Architecture_v1.0.png){ width=95% }

## 実装従属資料

本書の詳細は以下の5文書に分離する。これらは本書と同じく実装正本であり、矛盾時は「本書 v2.4 > 従属資料の最新版 > 旧資料」の順とする。

1. `HOMENECT_ERD_DB_Design_v1.0`
2. `HOMENECT_State_Transition_Business_Flow_v1.0`
3. `HOMENECT_API_Spec_v1.0` + `HOMENECT_OpenAPI_v1.0.yaml`
4. `HOMENECT_Screen_Detail_Spec_v1.0`
5. `HOMENECT_Development_Operations_Runbook_v1.0`

**Definition of Ready:** 上記6文書がLOCKED、P0の未確定値がConfig化され、法務項目はProduction Gateとして分離されている状態で実装開始可能とする。

# 01 / システム全体設計書

中核はチャネル非依存の HOMENECT CORE。Web/PWA が主要UIで、LINE/LIFFは入口・認証連携・通知アダプタとして利用する。

| **層**          | **標準案**                                               | **要件**                                           |
|-----------------|----------------------------------------------------------|----------------------------------------------------|
| Customer Web    | Next.js + TypeScript Responsive Web                                | ログイン/予約をLINE必須にしない。                  |
| Partner Web/PWA | Next.js同一Web + optional Manifest/Service Worker                        | 外部ブラウザでPWA。LIFF内でSW/A2HSを前提にしない。 |
| Admin           | Next.js Web Dashboard                                            | PC主、タブレット対応。                             |
| Backend/DB      | Supabase(PostgreSQL/Auth/Storage) + Next.js Server API + Edge Functions | **P0正式採用**。変更はChange Request。           |
| Channel Adapter | LINE Messaging/LIFF, Email, Web Push                     | 業務ロジックから分離。                             |
| Image           | Private Object Storage                                   | 公開URL禁止、短期署名URL。                         |
| Audit/Incident  | Append-only audit / incident log                         | 重要操作を追跡。                                   |

# 02 / プロジェクト概要書

| **項目**  | **定義**                                                                                                                    |
|-----------|-----------------------------------------------------------------------------------------------------------------------------|
| 目的      | 沖縄Pilot可能なエアコンクリーニング予約・施工・Partner Network基盤を完成。                                                  |
| 成功条件  | P0受入基準Pass、S1/S2=0、権限分離、Fallback、Backup/Restore、複数Partner E2E。                                              |
| Scope In  | Web予約、機器写真、Partner onboarding、案件提示/受諾/辞退、作業、現金、Preferred Area、Backup/HELP、通知コスト制御、Admin。 |
| Scope Out | オンライン決済、AI診断、動的価格、高度自動配車、会員制、全国自動最適化。                                                    |
| 事業前提  | 契約/価格/収益性はPilotで検証。設定値をハードコードしない。                                                                 |

# 03 / ユーザー・関係者定義

| **Actor**                     | **目的**                         | **権限/制約**                                    |
|-------------------------------|----------------------------------|--------------------------------------------------|
| Customer                      | 予約、確認、再予約               | 自分の顧客/機器/予約のみ。LINE利用必須ではない。 |
| Partner Owner/Admin           | 自社スタッフ・案件・売上管理     | 自社の情報と提示/割当案件。                      |
| Technician                    | 案件受諾、施工、記録             | 自分に提示/割当された案件のみ。                  |
| HOMENECT Admin                | 全体運用、例外、Partner/Area管理 | 個人情報は業務上必要な範囲。                     |
| Scheduler/Notification Engine | 通知・リマインド・期限           | 設定済みルールだけ実行。                         |
| Channel Provider              | LINE/Email/Push                  | 必要最小限のデータのみ。                         |

# 04 / 業務フロー

| **Step**       | **Actor**        | **Action**                           | **System Result**        |
|----------------|------------------|--------------------------------------|--------------------------|
| 1 流入         | Customer         | Web/QR/SNS/LINE等からアクセス        | source / session記録     |
| 2 初回入力     | Customer         | 機器写真・住所・希望枠               | Customer/Equipment作成   |
| 3 予約         | Customer         | 料金/契約主体/取消条件を確認して確定 | Reservation作成          |
| 4 ルーティング | System           | Area/技能/優先担当/空き判定          | JobOffer作成             |
| 5 受諾         | Partner          | 条件を確認し受諾/辞退                | 担当確定/Backupへ        |
| 6 施工         | Technician       | 前後写真・作業・異常                 | WorkLog保存              |
| 7 支払         | Customer→Partner | 現金                                 | CashReceipt保存          |
| 8 完了         | Technician       | 完了                                 | Repeat候補・レビュー依頼 |
| 9 HELP         | Partner          | 代行/応援/事故要請                   | 対象Partnerへ提示        |
| 10 再注文      | System/Customer  | 前回と同じ                           | 既存Equipment再利用      |

# 05 / 要件定義書

| **ID** | **Actor** | **機能**                | **要件**                                                      | **Priority** |
|--------|-----------|-------------------------|---------------------------------------------------------------|--------------|
| C01    | Customer  | Web閲覧/料金            | LINEなしでサービス/料金/対応範囲を閲覧                        | P0           |
| C02    | Customer  | 初回予約                | 写真・機器・住所/Area・希望枠                                 | P0           |
| C03    | Customer  | 空き/価格確認           | 設定可能な価格・空き枠を表示                                  | P0           |
| C04    | Customer  | 予約確認/取消           | 自分の予約を確認・取消                                        | P0           |
| C05    | Customer  | 任意LINE連携            | 予約後等にLINEを連携可能                                      | P0           |
| C06    | Customer  | 前回と同じ              | 同一機器の再入力省略                                          | P1           |
| C07    | Customer  | 再注文通知              | 6/12か月等を設定可能                                          | P1           |
| P01    | Partner   | Onboarding              | 法人/個人、保険/資格/条件を登録                               | P0           |
| P02    | Partner   | 稼働/Area/技能          | 受付ON/OFF、空き、Zone、技能                                  | P0           |
| P03    | Partner   | 案件オファー            | 日時/場所/内容/報酬/支払等を明示し証跡保存                    | P0           |
| P04    | Partner   | 受諾/辞退               | 案件単位で自由に判断                                          | P0           |
| P05    | Partner   | 作業報告                | 前後写真、時間、試運転、異常                                  | P0           |
| P06    | Partner   | 現金受領                | 受領額・時刻・精算対象                                        | P0           |
| P07    | Partner   | Preferred Area          | HOMENECT案件を優先ルーティング                                | P0           |
| P08    | Partner   | 優先担当                | preferred_partner_idで継続性を保持                            | P0           |
| P09    | Partner   | Backup/Overflow         | 辞退/満席時に次候補へ                                         | P0           |
| P10    | Partner   | HELP                    | 代行/応援/事故要請                                            | P0           |
| P11    | Partner   | PWA/Web Push            | 外部ブラウザでインストール/Push                               | P1           |
| A01    | Admin     | 顧客/予約               | 一覧/検索/編集/割当                                           | P0           |
| A02    | Admin     | Partner/Area            | Partner、Zone、技能、状態、優先度                             | P0           |
| A03    | Admin     | Notification Policy     | チャネル、LINE許可、費用、Fallback                            | P0           |
| A04    | Admin     | Communication Cost      | 送信数/推定費用/成果                                          | P1           |
| A05    | Admin     | KPI                     | 集客/利益/品質/供給/通信                                      | P1           |
| S01    | Platform  | 認証/権限               | Core IDとExternalIdentityを分離                               | P0           |
| S02    | Platform  | 監査                    | 料金/担当/状態/PII/設定                                       | P0           |
| S03    | Platform  | Idempotency             | 予約/通知/Webhook二重処理防止                                 | P0           |
| S04    | Platform  | Backup/Restore          | RPO/RTOと復元試験                                             | P0           |
| S05    | Platform  | Fallback                | LINE/Email/Push/DB障害時手動運用                              | P0           |
| S06    | Platform  | Channel Adapter         | LINE等を交換可能な疎結合                                      | P0           |
| C08    | Customer  | Partner変更希望         | 顧客が希望する場合、preferred_partner_idの変更申請/解除が可能 | P0           |
| P12    | Partner   | Relationship Protection | 顧客起点・優先担当・今回施工を分離し、HELP後の自動移管を防止  | P0           |
| P13    | Partner   | Anti-Circumvention      | HOMENECT由来顧客への迂回勧誘を禁止対象として記録/管理         | P0           |
| A06    | Admin     | Compliance Case         | 申告・証拠・Partner回答・判定・措置を管理                     | P0           |
| S07    | Platform  | PII staged disclosure   | 案件受諾前はPIIを最小化し受諾後に必要範囲だけ開示             | P0           |
| S08    | Platform  | Contact access audit    | 連絡先閲覧・担当変更・優先担当変更を監査                      | P0           |

# 06 / 機能一覧

| **Feature** | **名称**                                  | **対応要件** | **Priority** |
|-------------|-------------------------------------------|--------------|--------------|
| F-001       | Customer Web shell                        | C01,C02      | P0           |
| F-002       | Core identity & external identities       | C05,S01      | P0           |
| F-003       | Acquisition source capture                | C01          | P0           |
| F-004       | Customer/Equipment                        | C02          | P0           |
| F-005       | Private media upload                      | C02,S01      | P0           |
| F-006       | Availability/price engine                 | C03,P02      | P0           |
| F-007       | Reservation lifecycle                     | C02,C04      | P0           |
| F-008       | Partner onboarding                        | P01,A02      | P0           |
| F-009       | Partner availability/skills/area          | P02          | P0           |