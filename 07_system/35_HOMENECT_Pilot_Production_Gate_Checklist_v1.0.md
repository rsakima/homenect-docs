# HOMENECT Pilot / Production Gate Checklist v1.0

**Status: LOCKED / P0運用**

## Pilot Gate
- 実在Partner / 技能 / 保険
- 初期Area
- 料金 / fee / HELP payout / minimum margin Config
- 3グループ・7役割 / RLS / 自己承認制限テスト
- Customer本人確認E2E
- 予約・施工・現金・完了E2E
- HELP / Referral / Additional Work E2E
- Email / LINE / retry / fallback確認
- Incident drill
- Backup / Restore drill
- Pilot用規約・Privacy・キャンセル表示
- Open S1/S2 = 0

## Production Gate
- 法務専門家確認完了
- Admin / partner_admin MFA
- RLS / cross-tenant / PII / rate limit / upload / secret review
- Monitoring / Alert enabled
- Backup success + restore owner
- Rollback手順
- Production Config review
- Production LINE / Email / Supabase credentials
- 正式domain / HTTPS
- Data retention / deletion request / PII access procedure
- 運営・事故・緊急連絡体制
- Open S1/S2 = 0

Gate未達なら公開しない。例外は理由・影響・期限・責任者を記録する。
