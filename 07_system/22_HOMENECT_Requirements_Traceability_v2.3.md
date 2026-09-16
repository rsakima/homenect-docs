# HOMENECT Requirements Traceability v2.3

基準日: 2026-09-16  
Status: LOCKED / P0

Google Drive完成版 `HOMENECT_Requirements_Traceability_v2.3.xlsx` の実装ロック要約。

## v2.3追加トレース

| Requirement | Feature | Test | Acceptance | Priority |
|---|---|---|---|---|
| R-PP01 確定価格保護 | F-033 Price Protection | TC-027 | AC-21 | P0 |
| R-PP02 応援報酬分離 | F-034 HELP Payout | TC-028 | AC-22 | P0 |
| R-PP03 完全紹介再承認 | F-035 Referral Repricing | TC-029 | AC-23 | P0 |
| R-PP04 採算ガード | F-036 Margin Guard | TC-030 | AC-24 | P0 |
| R-PP05 追加作業承認 | F-037 Additional Work Approval | TC-031 | AC-25 | P0 |
| R-PP06 価格協議防止 | F-038 Price Privacy | TC-032 | AC-26 | P0 |
| R-PP07 契約責任再現 | F-039 Responsibility Snapshot | TC-033 | AC-27 | P0 |
| R-PP08 HELP関係維持 | F-017 + F-033 | TC-034 | AC-28 | P0 |

## Implementation Lock

- Reservation正式状態: REQUESTED / MATCHING / CONFIRMED / HELP_PENDING / REFERRAL_PENDING / IN_PROGRESS / INCIDENT_HOLD / COMPLETED / CANCELED
- ERD / DB設計: `25_HOMENECT_ERD_DB_Design_v1.0.md`
- 状態遷移: `26_HOMENECT_State_Transition_Business_Flow_v1.0.md`
- API/OpenAPI: `27_HOMENECT_API_Spec_v1.0.md` / `openapi/HOMENECT_OpenAPI_v1.0.yaml`
- Admin例外操作: Role + reason + immutable Audit
- P0は Requirement -> Feature -> Screen/API -> Test -> Acceptance の証跡がない限りCompleteにしない。
