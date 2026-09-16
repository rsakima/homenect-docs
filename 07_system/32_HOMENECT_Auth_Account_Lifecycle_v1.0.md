# HOMENECT ログイン・アカウント設計 v1.0

**Status: LOCKED / P0**

## まずここだけ
- 閲覧・空き確認: ログイン不要。
- 予約: `REQUESTED` 作成前に本人確認を完了する。
- Customer標準: メールOTP。
- LINE: 任意。LIFFで検証後に同一CustomerへExternalIdentityとして連携。
- 電話番号: P0では連絡先。認証IDにはしない。
- Partner / Admin: 招待制。
- `partner_admin` とPlatform AdminはProduction前MFA必須。

## Customer flow
1. サービス閲覧（匿名）
2. 予約入力
3. メールOTP、または任意のLINE本人確認
4. Supabase Auth session + Subjectを確立
5. Customerを作成/再利用
6. `POST /reservations` でREQUESTED作成
7. 以降の予約確認・取消・承認は同じ認証Subjectのownershipで制御

## Account lifecycle
`invited/pending -> active -> suspended -> revoked` を基本とする。Roleは別の`role_assignments`で管理する。

## Merge
名前・電話番号一致だけでは統合しない。複数Identity統合は双方の検証後のみ。Audit必須。

## Offboarding
Partner/Admin退職・契約終了時はRole Assignmentを即時revokedにし、必要に応じてAuth sessionを失効。履歴・監査は消さない。
