# HOMENECT 開発から公開までの流れ

**Version:** v1.0  
**基準日:** 2026-09-16  
**Status:** LOCKED / HUMAN-READABLE GUIDE  
**対象:** Product Owner / Claude Desktop・Claude Code / Codex / 開発担当者

## まずここだけ

HOMENECTは、次の流れで開発して公開します。

**作る → 自動チェック → 確認用サイトで見る → 本番公開を承認 → お客様向けに公開**

```text
Claude / Codexが開発
        ↓
作業ブランチへ保存
        ↓
自動チェック
        ↓
mainへ統合
        ↓
Stagingへ自動公開
        ↓
ブラウザで確認
        ↓
本番公開を承認
        ↓
同じCommitをProductionへ公開
        ↓
監視
```

## 1. 4つの場所

| 場所 | 何をする場所か | 誰が見るか |
|---|---|---|
| 開発環境 | Claude / Codexが作る | 開発者だけ |
| Preview | PRごとの確認 | 開発者・確認者 |
| Staging | 本番前の最終確認 | Product Owner・開発者 |
| Production | 実際のサービス | お客様・協力業者・運営 |

**重要:** `dev / staging / main` の3本の長期ブランチには分けません。Gitは `main + 短命の作業ブランチ` にします。Development / Staging / Productionは「動かす場所」として分けます。

## 2. 開発から公開まで

1. **Claude / Codexが作る**  
   `feat/...` などの作業ブランチで開発します。mainを直接編集しません。

2. **途中でもGitHubへ保存する**  
   Token上限や交代に備え、小さな区切りでcommit + pushします。

3. **自動チェックする**  
   lint、型チェック、テスト、DB変更確認、権限テスト、OpenAPI、build、重要E2Eを実行します。

4. **Pull Requestでmainへ統合する**  
   1 PR = 1目的を原則にします。

5. **Stagingへ自動公開する**  
   mainへ統合した最新版を、確認用サイトへデプロイします。

6. **ブラウザで確認する**  
   お客様、協力業者、運営の主要な操作を実際の画面で確認します。

7. **本番公開を承認する**  
   問題がなければProductionへの公開を承認します。

8. **同じCommitをProductionへ出す**  
   Stagingで確認したのと同じGit commitを本番へ出します。Stagingのファイルを手作業でコピーしません。

9. **公開後を監視する**  
   エラー、ログイン、通知、LINE、DB、Storage、Backupなどを監視します。

## 3. Product Ownerがすること

Product Ownerが毎回行うのは、原則として次の2つです。

- **Stagingをブラウザで見て確認する**
- **Productionへ公開してよいか承認する**

実装、テスト、Git操作、差分確認、Handoff更新はClaude / Codex側で行います。

## 4. ClaudeとCodexが途中交代するとき

```text
Claudeが作業
  ↓
commit + push
  ↓
AI_HANDOFF.mdを更新
  ↓
CodexがGitを取得
  ↓
Handoff / 差分 / テスト結果を確認
  ↓
同じ作業の続きを開始
```

逆の交代も同じです。

- チャット履歴を正本にしません。
- 同じbranchを2つのAIが同時編集しません。
- 交代前に作業をGitHubへ残します。

## 5. DB変更がある場合

DB変更は、StagingとProductionへそれぞれMigrationを適用します。

安全のため、原則として次の順にします。

**新しいDB構造を追加 → アプリを更新 → 動作確認 → 後から古い構造を整理**

本番DBをその場で手作業変更する運用にはしません。

## 6. 問題が起きたとき

- Stagingで問題が見つかった → Productionへ出さず修正します。
- Productionのアプリで重大な問題 → 直前の安定版へRollbackします。
- DB変更を単純に戻せない → データを守りながらForward Fixします。
- S1 / S2の重大不具合が残る → 本番公開しません。

## 7. コストを増やしすぎない

- 開発はPC上を基本にします。
- Previewは必要な時だけ使います。
- Stagingは最小構成にします。
- Productionだけ安定運用を優先します。

「環境を分ける = サーバー代が3倍」にはしません。

## 8. 最終ルール

**Git:** `main + 短命feature/fix/chore branch`  
**環境:** Development / Preview / Staging / Production  
**Staging:** mainの最新版を自動デプロイ  
**Production:** Staging確認済みの同一commitを手動承認でデプロイ  
**AI交代:** Git + `docs/AI_HANDOFF.md`  
**Product Owner:** Staging確認とProduction公開承認を中心に行う

技術的な詳細は `HOMENECT_Development_Operations_Runbook_v1.0` と `HOMENECT_AI_Collaborative_Development_Protocol_v1.0` を参照します。
