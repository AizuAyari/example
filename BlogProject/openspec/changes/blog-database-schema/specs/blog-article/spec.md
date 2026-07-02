## ADDED Requirements

### Requirement: 記事データモデル
システムは `Article` モデルを提供しなければならない（MUST）。`Article` は以下のフィールドを持つ:
- `title`: 記事タイトル（文字列、必須）
- `content`: 記事本文（テキスト、必須）
- `author`: `User` への外部キー（`on_delete=CASCADE`、必須）
- `created_at`: 作成日時（`auto_now_add=True` で自動設定、編集不可）
- `updated_at`: 更新日時（`auto_now=True` で保存の度に自動更新）

#### Scenario: 記事作成時に作成日時が自動設定される
- **WHEN** 認証済みユーザーが新しい記事を作成する
- **THEN** `created_at` フィールドが現在日時で自動的に設定される

#### Scenario: 記事更新時に更新日時が自動更新される
- **WHEN** 既存の記事の `title` または `content` が更新され保存される
- **THEN** `updated_at` フィールドが更新時点の現在日時に自動更新される（`created_at` は変化しない）

#### Scenario: 著者情報のない記事は作成できない
- **WHEN** `author` を指定せずに `Article` を保存しようとする
- **THEN** データベース制約によりエラーとなり記事は作成されない

### Requirement: 記事一覧のデフォルト並び順
記事一覧はデフォルトで投稿日時の降順（新しい順）で表示されなければならない（MUST）。

#### Scenario: 明示的な並び順指定なしでの一覧取得
- **WHEN** クエリで明示的な `order_by()` を指定せずに `Article.objects.all()` を取得する
- **THEN** 結果は `created_at` の降順（最新の記事が先頭）で返される

### Requirement: 記事の管理画面表示
`Article` モデルは管理画面（Django Admin）で識別しやすい文字列表現を持たなければならない（MUST）。

#### Scenario: 管理画面での記事表示
- **WHEN** 管理者が Django Admin の記事一覧画面を開く
- **THEN** 各記事はタイトルで識別可能な形式で表示される（`__str__()` がタイトルを返す）
