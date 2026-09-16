# HOMENECT 正式開発発注仕様書

> **同期元:** `15_開発会社向け正式資料/HOMENECT_Formal_Development_Order_Spec_v2.1.docx` / 2026-09-16 完成版

> Formal Development Order Specification v2.1 / 2026-09-16

> Web First / PWA Optional / LINE Connected / Partner Network / Relationship Protection

> FOR VENDOR / FORMAL

## 01. Project Overview

### 1.1 Project Name

HOMENECT

### 1.2 Objective

沖縄でエアコンクリーニングから開始するHomeCare NetworkのMVPを構築します。Customerの集客・予約・機器写真・施工履歴・再注文、Partnerの案件受諾・施工記録・availability、Adminの予約・顧客・Partner・Area・例外運用を一元管理し、将来の複数Partner・複数地域・複数HomeCareカテゴリへ拡張可能なCoreを構築します。

v2.1ではWeb First / PWA Optional / LINE Connectedを採用し、LINEを必須UI・必須identityにしません。Preferred Area / Backup / HELP、Customer Relationship Protection、Anti-Circumvention、staged PII、Compliance CaseをP0へ追加します。

### 1.3 Formal Business Source of Truth

事業Source of TruthはHOMENECT Business Concept Master v2.2です。同書は2026-09-15正式原本 Business Concept Master v2.0を事業原点として維持し、その後の承認Decisionを正式統合したものです。

### 1.4 Current State

- Production未開始。
- Pilot前。
- 価格、Partner報酬、HOMENECT fee等は未確定でありConfig化対象。
- 実在Partner / Backup Partner / insurance / qualification等はLaunch Gateで確認。
- 本仕様は開発会社への見積・設計・実装・試験・検収基準。

### 1.5 Delivery Principle

Vendorはまず差分・不明点・Blockerを整理し、P0見積、P1 Option見積を分離してください。未確定Business valueを開発判断で固定しないでください。

## 02. Reference Architecture

### 2.1 Architecture Decision

**Channel-Independent Web Platform**

- Customer：Responsive Web。
- Partner：Responsive Web / optional PWA。
- Admin：Web Dashboard。
- LINE：optional identity / LIFF entry / messaging channel。
- Email：standard notification channel。
- Web Push：optional low-cost channel。
- Core：Channel independent business logic and data。

### 2.2 Reference Stack

標準候補：

- PostgreSQL / Supabase。
- Supabase Auth。
- Supabase Storage private bucket。
- Edge Functions等server-side API。
- Responsive Web frontend。
- PWA manifest / service worker（Partner P1）。
- LINE Messaging API / LIFF adapter。
- Email provider adapter。
- Web Push adapter。

Vendorは同等以上の構成を提案可能です。差替え時はsecurity、cost、operation、migration、vendor lock-in、Japan region / data residency等を比較してください。

### 2.3 Architecture Guardrails

- LINE userIdをCustomer/Partner core PKにしない。
- Business logicをLINE webhook内へ集中させない。
- CustomerはLINE unavailableでも主要業務完了可能。
- PartnerはPWA installなしでも主要業務完了可能。
- LIFF browser内でService Worker / A2HS依存にしない。
- Channel adapterを疎結合化。

## 03. Actors / Permissions

### Customer

- own customer / equipment / reservation only。
- own image / work summary access。
- optional LINE link / unlink。
- preferred Partner change request。

### Partner Owner / Admin

- own Partner profile / users / availability / area / service skills。
- offers presented to Partner。
- accepted / assigned reservations。
- own work / cash / HELP records。

### Technician

- accepted / assigned jobs only。
- minimum customer PII after acceptance。
- WorkLog / photos / incident / CashReceipt。

### HOMENECT Admin

- operational global access according to Admin role。
- Customer / Reservation / Partner / Area / Notification Policy / Incident / Compliance / Audit。

### System Actors

- Scheduler。
- Notification Engine。
- Webhook processors。

## 04. E2E Business Flow

1. Customer enters Web from acquisition source。
2. Service / area / price info。
3. Customer / Equipment / photos。
4. availability check。
5. confirmation before order。
6. Reservation created with idempotency。
7. Customer optional LINE link。
8. route by Area / skills / preferred Partner / capacity。
9. create JobOffer with terms snapshot。
10. Partner accepts / declines。
11. if decline / timeout, Backup / Overflow。
12. after Accept, disclose required PII。
13. Work start / Before photo。
14. service / abnormality handling。
15. After / test operation / WorkLog。
16. Customer pays Partner cash in MVP。
17. CashReceipt record。
18. Complete。
19. P1 repeat / reminder / KPI。
20. If Partner needs support: HELP flow。
21. If incident: Incident flow。
22. If customer circumvention allegation: Compliance Case flow。

## 05. Functional Requirements

### Customer

#### C01 Web閲覧/料金 P0

LINEなしでservice、price、service areaを閲覧可能。

#### C02 初回予約 P0

Customer、Equipment、photo、area、requested slotを登録。

#### C03 空き/価格確認 P0

configurable price / availability表示。

#### C04 予約確認/取消 P0

Customer own reservations view / cancel。

#### C05 optional LINE link P0

Core customer identityを維持したままLINE external identity link可能。

#### C06 same-as-before P1

Existing Equipment / previous serviceを再利用。

#### C07 repeat reminder P1

6 / 12 months等configurable reminder。

#### C08 Partner change request P0

Customer requestによりpreferred_partner_idを変更/解除可能。理由・actor・timestampをaudit。

### Partner

#### P01 Onboarding P0

legal name / entity type / insurance / qualifications / services / areas / agreement version。

#### P02 Availability / Area / Skills P0

accepting ON/OFF、capacity、time slots、blackout、service skills、AreaZone。

#### P03 Job Offer P0

Partnerへdatetime、approx location、service/work、compensation、payment conditions等を明示。Terms Snapshot保存。

#### P04 Accept / Decline P0

Offerごとに自由にaccept / decline。response / timestamp保存。

#### P05 WorkLog P0

Before / After photos、start/end、test operation、abnormality、comments。

#### P06 Cash Receipt P0

amount、received_at、status、reservation relation。

#### P07 Preferred Area P0

HOMENECT-origin jobsのpriority routing。

#### P08 Preferred Partner P0

Customer continuity。Customer property rightではない。

#### P09 Backup / Overflow P0

decline / timeout / no capacity時next candidate。

#### P10 HELP P0

overdemand、absence、complex machine、technical help、incident等。

#### P11 Partner PWA / Web Push P1

external browser installability / push。not mandatory。

#### P12 Relationship Protection P0

relationship source、origin_partner、preferred_partner、service_partnerを分離。HELP aloneでpreferred自動変更禁止。

#### P13 Anti-Circumvention P0

HOMENECT-origin customer contactを利用したoff-platform solicitationをpolicy / contract対象として管理。

### Admin

#### A01 Customer / Reservation P0

list、search、detail、edit with audit、assignment / exception operation。

#### A02 Partner / Area P0

Partner、PartnerUser、skills、insurance metadata、AreaZone、PartnerArea、priority、status。

#### A03 Notification Policy P0

channel、event、cost class、fallback、paid LINE restriction。

#### A04 Communication Cost P1

send units / estimated cost / outcome。

#### A05 KPI P1

acquisition、reservation、contribution、quality、supply、notification cost。

#### A06 Compliance Case P0

allegation、evidence、Partner response、decision、action、status。

### Platform

#### S01 Auth / Authorization P0

Core SubjectとExternalIdentity分離。RBAC / RLS等。

#### S02 Audit P0

price、assignment、status、PII、permission、configuration等。

#### S03 Idempotency P0

reservation creation、webhook、notification、critical state transition。

#### S04 Backup / Restore P0

RPO / RTO and restore test。

#### S05 Fallback P0

LINE / Email / Push / DB / system incident manual continuation plan。

#### S06 Channel Adapter P0

LINE / Email / Push swap / extension。

#### S07 Staged PII Disclosure P0

Before acceptance PII minimal / masked。After Accept required only。

#### S08 Contact Access Audit P0

contact / detailed address / preferred assignment change / sensitive access audit。

## 06. Feature Breakdown

### P0 Features

- F-001 Customer Web shell。
- F-002 Core identity & ExternalIdentity。
- F-003 Acquisition source capture。
- F-004 Customer / Equipment。
- F-005 Private media upload。
- F-006 Availability / price engine。
- F-007 Reservation lifecycle。
- F-008 Partner onboarding。
- F-009 Partner availability / skills / area。
- F-010 Preferred Area router。
- F-011 Preferred Partner continuity。
- F-012 Job Offer / Terms Snapshot。
- F-013 Accept / Decline / Expiry。
- F-014 Overflow / Backup queue。
- F-015 WorkLog / photos。
- F-016 CashReceipt。
- F-017 HELP。
- F-018 Notification Engine。
- F-019 LINE adapter / LIFF entry。
- F-020 Email adapter。
- F-021 Audit / Incident。
- F-022 Backup / Restore。
- F-023 Admin Console。
- F-028 Customer Relationship source & continuity。
- F-029 Anti-Circumvention policy / case trigger。
- F-030 staged PII disclosure。
- F-031 Compliance Case management。
- F-032 Contact / Assignment access audit。

### P1 Features

- F-024 PWA / Web Push。
- F-025 Repeat / same-as-before / reminder。
- F-026 Communication Cost Ledger。
- F-027 KPI Dashboard。

## 07. Screen List

### Customer

- CUS-001 service / pricing landing。
- CUS-002 equipment / photos。
- CUS-003 availability。
- CUS-004 booking confirmation。
- CUS-005 reservation list / detail / cancel。
- CUS-006 optional LINE link。
- CUS-007 repeat P1。
- CUS-008 preferred Partner change request / support entry。

### Partner

- PAR-001 Partner Home / accepting ON/OFF。
- PAR-002 Job Offer / Accept / Decline。
- PAR-003 Today Jobs。
- PAR-004 Work Report / photos / CashReceipt。
- PAR-005 HELP。
- PAR-006 Schedule / availability。
- PAR-007 Sales / settlement P1。
- PAR-008 Incident / support。

### Admin

- ADM-001 Dashboard。
- ADM-002 Reservations。
- ADM-003 Customer / Equipment / relationship。
- ADM-004 Partner / Area / skills。
- ADM-005 Notification Policy。
- ADM-006 Incident / Audit。
- ADM-007 KPI / Cost P1。
- ADM-008 Compliance Cases。

## 08. UI / UX Requirements

- Mobile First for Customer / Partner。
- desktop responsive for Admin。
- Customer does not require PWA install。
- Partner does not require PWA install。
- main CTA obvious。
- avoid technical jargon。
- progressive disclosure。
- accessible tap targets / keyboard / contrast as practical。
- error state tells next action。
- loading / retry state for image upload。
- confirmation before irreversible actions。
- price / final terms clearly visible before booking / Accept。
- review flow must not implement positive-only public review routing。

## 09. Data Model

### Customer

id、contact fields、area、consent、preferred_partner_id等。

### ExternalIdentity

subject_type、subject_id、provider、provider_user_id、verified_at。

### Equipment

customer_id、room、maker、model、type、notes、last_service_at。

### Partner

legal_name、entity_type、status、insurance、qualifications、agreement_version。

### PartnerUser

partner_id、role、status。

### AreaZone

code、postal / municipality / geometry等。

### PartnerArea

partner_id、zone_id、priority、skills、capacity。

### Reservation

customer、equipment、service、requested slot、price snapshot、status、source、service partner等。

### JobOffer

reservation、partner、terms_snapshot、presented_at、expires_at、response、response_at。

### WorkLog

reservation、technician、before / after、start / end、test、abnormality、comment。

### HelpRequest

reservation、requester、type、target、status、terms。

### CashReceipt

reservation、amount、received_at、status。

### Notification

event、channel、cost_class、provider result、idempotency_key。

### CommunicationCost P1

notification、units、estimated_cost、outcome。

### CustomerRelationship

customer_id、source_type、origin_partner_id、preferred_partner_id、updated_reason。

### ComplianceCase

customer、partner、reservation、allegation、evidence、partner_response、decision、action、status。

### PIIAccessEvent

actor、customer、reservation、field_scope、reason、occurred_at。

### Incident

reservation、severity、category、summary、status。

### AuditEvent

actor、action、entity、before / after、occurred_at。

## 10. Logical API

Implementation may alter route naming but must preserve responsibilities.

### Customer

- `POST /api/reservations`
- `GET /api/availability`
- `GET /api/reservations/{id}`
- `POST /api/reservations/{id}/cancel`
- `POST /api/identity/line/link`
- `POST /api/customer/preferred-partner/change-request`

### Partner

- `GET /api/partner/offers`
- `POST /api/partner/offers/{id}/accept`
- `POST /api/partner/offers/{id}/decline`
- `PUT /api/partner/availability`
- `POST /api/worklogs`
- `POST /api/help`
- `POST /api/cash-receipts`
- `POST /api/incidents`

### Admin

- `/api/admin/customers*`
- `/api/admin/reservations*`
- `/api/admin/partners*`
- `/api/admin/areas*`
- `/api/admin/notification-policy*`
- `/api/admin/incidents*`
- `/api/admin/compliance*`
- `/api/admin/audit*`

### Integration

- `POST /webhooks/line`
- notification worker / job。
- email provider callback if needed。

## 11. Non-Functional Requirements

### NFR-01 API

major non-image API P95 <= 1.5 seconds target under initial load profile。

### NFR-02 Web UX

main Customer / Partner Web usable state P95 <= 3 seconds target under defined network/device profile。

### NFR-03 Availability

Pilot / commercial monthly availability target >= 99.5%，excluding agreed maintenance / external outage conditions defined in SLA。

### NFR-04 Capacity

initial engineering target：100 reservations/day、Partner20、Technician100 without architectural rewrite。Actual Pilot will replace assumptions。

### NFR-05 Media

max original upload 10MB/image initial candidate。compress / resize / quota monitor。

### NFR-06 Backup

initial RPO <= 24h / RTO <= 4h target。Restore test before Pilot。

### NFR-07 Browser

latest 2 generations where practical：iOS Safari / Chrome、Android Chrome、desktop Chrome / Edge。LINE in-app browser for basic compatible flow。

### NFR-08 PWA

Partner external browser installability P1。All core P0 functions usable without install。

### NFR-09 Maintainability

price、fee、capacity、area priority、notification policy、reminder interval等Config化。

### NFR-10 Cost Observability

channel usage / estimated variable cost P1。P0 logs enough data for later calculation。

## 12. Security Requirements

### SEC-01 Authentication / Authorization

Customer / Partner / Admin separation。RLS / server-side ownership validation。

### SEC-02 Admin / Partner Owner

commercial launch before strong authentication / MFA where supported and operationally feasible。

### SEC-03 Tenant / Assignment Boundary

Partner cannot read other Partner customers / jobs unless explicit HELP / assignment grants access。

### SEC-04 Staged PII

Before acceptance do not reveal unnecessary full name / phone / detailed address。

### SEC-05 Media

private storage、short-lived signed URL、MIME / size / authorization validation。

### SEC-06 Secrets

server side only。No API secrets in client bundle / repo / public config。

### SEC-07 Audit

price、assignment、status、PII access、permission、policy、customer relationship changes。

### SEC-08 LINE

webhook signature / token verification server-side。Do not trust raw client-submitted provider identity。

### SEC-09 Incident

PII leak / wrong notification / cross-tenant access S1/S2 candidate。

### SEC-10 Rate / Abuse

booking、auth、upload、webhook、admin actionsにreasonable abuse protection。

## 13. Test Cases

### TC-001

Web new booking -> offer -> accept -> service -> cash -> complete。

### TC-002

Booking completes without LINE。

### TC-003

Optional LINE linking retains same Customer; no duplicate Customer。

### TC-004

Preferred Area routing selects expected candidate set / order。

### TC-005

Preferred Partner unavailable -> Backup / Overflow。

### TC-006

Partner decline -> next candidate; no forced acceptance side effect。

### TC-007

JobOffer terms snapshot reproducible after accept / decline。

### TC-008

HELP service preserves relationship unless Customer choice changes it。

### TC-009

Partner cross-customer access -> 403 / masked。

### TC-010

Private image permission / signed URL expiry。

### TC-011

Capacity / concurrent booking avoids overbooking。

### TC-012

Webhook / request replay no duplicate reservation / notification。

### TC-013

Paid LINE Push to unconverted lead blocked by policy。

### TC-014

Important notification fallback executes when primary fails per policy。

### TC-015

LIFF browser basic core flow works without Service Worker dependency。

### TC-016

Partner external-browser PWA install P1 / no conflict with normal Web。

### TC-017

Incident prevents incorrect normal completion where configured and creates Incident record。

### TC-018

Backup restore preserves critical relationship。

### TC-019 P1

same-as-before reuses Equipment and pricing / service rules correctly。

### TC-020 P1

CommunicationCost matches Notification units / configured pricing model。

### TC-021

HELP substitute does not automatically transfer preferred Partner。

### TC-022

Customer change request can update / clear preferred Partner and logs change。

### TC-023

Before Accept PII is masked / minimized。

### TC-024

After Accept only required PII shown and access audited。

### TC-025

Circumvention allegation -> ComplianceCase -> evidence -> Partner response -> decision -> action audit。

### TC-026

Unsubstantiated allegation does not auto-ban Partner。

## 14. Acceptance Criteria

### P0 Acceptance

- AC-01 Customer can book without LINE。
- AC-02 first-time images private / retryable。
- AC-03 before booking finalization, service / quantity / price / datetime / payment / cancellation / contract party shown per final business/legal spec。
- AC-04 Partner can accept / decline offer。
- AC-05 multiple Partners work through Preferred Area / Backup。
- AC-06 JobOffer conditions retained。
- AC-07 Before / After / abnormality / test operation stored。
- AC-08 CashReceipt related to Reservation。
- AC-09 HELP supports substitute / assistance flow。
- AC-10 cross-Customer / cross-Partner unauthorized data inaccessible。
- AC-11 paid LINE lead push blocked by default policy。
- AC-12 core Web flow survives LINE outage / unavailable state。
- AC-13 Audit visible to authorized Admin。
- AC-14 Backup restore pass。
- AC-15 S1 / S2 open defects = 0 at acceptance。
- AC-16 environment / operations / incident / config / open gate docs delivered。
- AC-17 origin / preferred / service Partner separated; HELP alone does not transfer preferred。
- AC-18 Customer can request preferred Partner change / removal。
- AC-19 staged PII + access audit passes。
- AC-20 Compliance Case supports evidence / response / human decision / staged action。

### P1 Acceptance

PWA / Push、Repeat、Cost Ledger、KPIはOption acceptanceを別途定義。

## 15. Infrastructure / Environment

### Development

- dummy / synthetic data。
- development channel credentials only。
- no production customer data。

### Staging

- realistic test data。
- staging LINE / email / push credentials if available。
- E2E / acceptance test。

### Production

- separate DB / secrets / storage / domain。
- backup / monitor / alert。
- migration versioned。

### CI / CD

- Git / PR。
- schema migrations。
- staging before production。
- rollback plan。

## 16. Operations / Fallback

### Normal

Human on Exception。

### LINE outage

Customer / Partner direct Web remains accessible。No data corruption。Queued / failed notification visible / retryable according to policy。

### Email / Push outage

fallback per priority / important condition。

### Core outage

read-only / manual fallback procedure documented where feasible; restore / incident process。

### Partner no-show / absence

Admin / HELP / Backup route。

### Incident

S1 / S2 immediate escalation and evidence preservation。

### PII incident

access revoke、affected scope、timeline、notification / authority response according to final legal policy。

## 17. Development Milestones

### M0 Requirements Lock

- v2.1 delta review。
- Open Questions。
- WBS / estimate。
- legal / business gates identified。

### M1 Core / Identity

- Web shell。
- DB / migrations。
- Auth / RLS。
- Customer / ExternalIdentity。
- private storage。
- adapter interfaces。

### M2 Booking / Partner

- Customer / Equipment / photos。
- availability / price。
- Reservation。
- Partner / Area / skills / capacity。
- JobOffer / accept / decline。
- WorkLog / Cash。

### M3 Network / Relationship

- Preferred Area。
- preferred / origin / service Partner。
- Backup / Overflow。
- HELP。
- staged PII。
- Notification Policy。
- Compliance Case。

### M4 E2E / Hardening

- tests。
- security review。
- performance。
- incident / restore。
- defect fix。

### M5 Handover / Production Ready

- P0 AC pass。
- docs。
- runbook。
- staging / production setup。
- launch gates not confused with software completeness。

### P1 Option

- PWA / Web Push。
- Repeat / reminders。
- Communication Cost Ledger。
- KPI Dashboard。

## 18. Risk / Issue Requirements

Vendor shall maintain project risk / issue register including：

- schedule / dependency。
- security / privacy。
- channel external dependency。
- data migration / schema。
- browser / LIFF differences。
- Partner relationship / PII boundaries。
- config / unknown business value。
- performance / media cost。

Business/legal risks are controlled via Business Master gates and are not silently resolved by code assumptions。

## 19. Change Control

### Source-controlled artifacts

- requirement IDs。
- schema / migration。
- API contract。
- test cases。
- decision log。
- change log。

### Change Request

Any scope / acceptance / data model / security / external integration change shall state：

- requested change。
- reason。
- affected requirements。
- estimate / schedule impact。
- migration / compatibility impact。
- test / acceptance impact。
- approval status。

## 20. Decision Log

### Adopted

- HOMENECT Brand。
- Web First Customer。
- optional PWA Partner。
- LINE Connected Channel。
- Preferred Area。
- preferred Partner continuity。
- Backup / HELP。
- Relationship Protection。
- Anti-Circumvention guardrails。
- Customer Choice。
- staged PII。
- Compliance due process。
- MVP cash direct Customer -> Partner。
- configuration over hardcoded unknowns。

### Rejected / Deferred

- mandatory native app MVP。
- LINE as Core PK / only UI。
- fixed 20% fee。
- paid LINE Push to unconverted leads by default。
- exclusive Partner territories。
- automatic preferred transfer after HELP。
- automatic severe penalty on allegation only。
- review gating。

## 21. Open Gates / Non-Coding Decisions

### G-01 Pricing / payout / fees

Business owner before Pilot/production config freeze。

### G-02 Contract Party

Legal/business final display and terms。

### G-03 Area / Customer / competition rules

Legal review before Pilot partner network use。

### G-04 Partner insurance / qualification

Operational real-world verification。

### G-05 Freelance transaction conditions

Legal + technical evidence format review。

### G-06 Cancellation / warranty / refund

Business/legal before production。

### G-07 Backup Partner

real available Partner + E2E。

### G-08 Privacy / Terms / Partner Data Access

legal/security before real data。

### G-09 Communication Provider / Cost

LINE / Email / Web Push actual price and plan review。

### G-10 Backup / Restore / Monitoring

technical launch gate。

### G-11 Trademark / Domain

HOMENECT public release before final brand lock。

### G-12 Anti-Circumvention Contract

scope、duration、sanction、liquidated damages if any、customer choice compatibility、competition law / contract enforceability reviewed by qualified counsel。

### G-13 Repeat / HELP Economics

Pilot validates fee model does not create excessive incentive for off-platform circumvention。

## 22. Requirements Traceability

Vendor shall use accompanying `HOMENECT_Requirements_Traceability_v2.1.xlsx` as requirements register and trace：

**Requirement -> Feature -> Screen/API -> Test -> Acceptance**

No P0 requirement may be marked Complete without mapped verification。

## 23. Vendor Deliverables

Required：

1. Requirements delta / questions。
2. architecture / data model / ERD。
3. detailed estimate P0 / P1 separate。
4. implementation source repository。
5. migrations。
6. environment config template (no secrets)。
7. unit / integration / E2E test results。
8. security verification report。
9. performance check result。
10. staging deployment。
11. production deployment / handover if contracted。
12. backup / restore evidence。
13. operations runbook。
14. open issues / known limitations。
15. requirement traceability updated。
16. change / decision records。

## 24. Out of Scope Unless Approved

- native iOS / Android app。
- online payment production implementation。
- non-aircon categories production rollout。
- AI recommendation / dynamic pricing。
- complex marketplace escrow。
- Partner employment / payroll system。
- accounting system replacement。
- CRM / marketing automation beyond defined notification / acquisition tracking。

## 25. Estimation Request

Vendor estimate shall separate：

### P0 Must

- Web Customer / Partner / Admin。
- Core Identity / DB / Storage。
- Booking / Area / Partner / JobOffer / WorkLog / Cash。
- Backup / HELP。
- LINE optional integration / email notification baseline。
- Notification policy。
- Relationship Protection / staged PII / Compliance Case。
- Security / Audit / Backup / Fallback。
- Tests / Acceptance / deployment / documentation。

### P1 Option

- Partner PWA / Web Push。
- Repeat / reminder automation。
- Cost Ledger。
- KPI Dashboard。
- advanced settlement views。

Vendor shall identify dependencies, risks, assumed external fees, and items requiring Product Owner decision before fixed estimate。
