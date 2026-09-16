# HOMENECT 権限実装仕様 v1.0

**Status: LOCKED / P0**

## まずここだけ
利用者は「お客様・協力業者・HOMENECT運営」の3グループ、内部は7役割です。1人1アカウントで複数役割を持てます。権限はdeny-by-defaultとし、重要操作はAuditします。

## 7役割
| グループ | 表示名 | 内部コード | 主な範囲 |
|---|---|---|---|
| お客様 | お客様 | `customer` | 自分の予約・機器・承認 |
| 協力業者 | 協力業者管理者 | `partner_admin` | 自社管理・案件受諾・HELP |
| 協力業者 | 作業スタッフ | `technician` | 担当案件の施工・記録 |
| HOMENECT運営 | 運営管理者 | `ops_admin` | 予約・割当・HELP・Referral |
| HOMENECT運営 | 経理管理者 | `finance_admin` | 売上・精算・報酬・補填 |
| HOMENECT運営 | 事故・コンプライアンス管理者 | `compliance_admin` | 事故・苦情・違反調査 |
| HOMENECT運営 | 最高管理者 | `super_admin` | 権限・重要設定・緊急例外 |

## 実装ロック
- `role_assignments(subject_id, role_code, scope_type, scope_id, status, granted_by, granted_at, revoked_at)` をP0に含める。
- Partner Roleは `scope_type=partner` + `scope_id=partner_id` 必須。
- Platform Adminは `scope_type=platform`。
- Customerは `scope_type=self`。
- `partner_admin` と `technician` は兼任可。管理者権限だけで施工権限を暗黙付与しない。
- UIだけでなくAPI / Use Case / RLSで強制。
- role変更、重要PII閲覧、価格・補填・Compliance・緊急例外はAudit。
- 高リスク操作は自己承認禁止。Pilot例外は `reason + audit + 後日レビュー`。
