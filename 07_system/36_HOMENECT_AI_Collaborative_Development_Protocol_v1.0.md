# HOMENECT AI共同開発ルール

**Version:** v1.0  
**基準日:** 2026-09-16  
**Status:** LOCKED / P0開発運用ルール

## まずここだけ

HOMENECTは、**Claude Desktop / Claude Code / Codexのどれが途中から入っても、チャット履歴なしで開発を続けられる**運用にする。

そのために、開発の現在地をGitへ残す。

1. 1タスクを小さくする。
2. 同じbranchを2つのAIが同時編集しない。
3. 区切りごとにcommit + pushする。
4. 止まる前に`docs/AI_HANDOFF.md`を更新する。
5. 次のAIはHandoff・last commit・diff・test結果を確認して続ける。

## 1. 正本

| 内容 | 正本 |
|---|---|
| 事業・仕様・正式Decision | `rsakima/homenect-docs` |
| 実装コード | `rsakima/homenect` |
| 現在の開発状態 | `rsakima/homenect/docs/AI_HANDOFF.md` |
| AI共同開発の詳しい手順 | `rsakima/homenect/docs/AI_DEVELOPMENT_PROTOCOL.md` |

チャットの記憶だけを正本にしない。

## 2. AI交代時

### 前のAI

- 変更を小さくcommitする。
- remoteへpushする。
- テスト結果を残す。
- Handoffへ「次にすること」を1つ書く。

### 次のAI

- `git fetch`する。
- Handoffを読む。
- branchとlast commitを確認する。
- diffを確認する。
- 必要なテストだけ再確認する。
- 続きを実装する。

## 3. Token節約

毎回すべての資料を全文読まない。

**Search → 必要な箇所だけ読む → 既存を再利用 → 最小変更 → 必要なテスト → Diff → Handoff**

の順で進める。

## 4. Branch

原則 `1 PR = 1目的`。

例：

- `feat/p0-bootstrap`
- `feat/p0-customer-auth`
- `feat/p0-partner-rbac`
- `feat/p0-reservation-request`

同一branchは同時に1エージェントだけが編集する。

## 5. 途中終了

Token切れや作業時間終了でも、feature branchではcheckpoint commitを許可する。

例：

`WIP checkpoint: reservation migration before RLS`

ただし、重要な変更をローカルだけに残さない。

## 6. 人間への質問

Product Ownerは原則、意思決定だけを行う。

既存仕様で決められることはAIが処理する。
Business / Legal / Financial / Product Scopeの判断が必要な場合だけ、推奨付きA〜Eの5択で確認する。

## 7. 人間向け資料

人間が読む資料は難しくしない。

- 日本語を主表示
- 最初に「まずここだけ」
- 短い文章
- 表と具体例を優先
- DB名・API・内部コードは開発者向け補足へ分離

## 8. 正式決定

HOMENECTのP0開発は、**Gitを共通記憶としてClaudeとCodexが交代可能な運用**を正式採用する。

エージェント固有のチャット履歴へ依存せず、コード・commit・test・Handoffから再開できることをDone条件の一部とする。
