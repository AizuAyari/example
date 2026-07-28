## ADDED Requirements

### Requirement: キーワードデータモデル（Phase 2）
システムは記事にキーワードタグを付与するための `Keyword` モデルを提供しなければならない（MUST）。`Keyword` は以下のフィールドを持つ:
- `keyword_text`: キーワード文字列（必須）
- `article`: `Article` への外部キー（必須）

#### Scenario: 記事にキーワードを追加する
- **WHEN** 既存の記事に対して `keyword_text` を指定した `Keyword` レコードを作成する
- **THEN** 当該 `Keyword` レコードが対象の `Article` に紐づいた状態で保存される

#### Scenario: 記事削除時のキーワード連鎖削除
- **WHEN** ある `Article` がデータベースから削除される
- **THEN** その記事に紐づく全ての `Keyword` レコードも削除される

### Requirement: キーワードの管理画面表示
`Keyword` モデルは管理画面（Django Admin）で識別しやすい文字列表現を持たなければならない（MUST）。

#### Scenario: 管理画面でのキーワード表示
- **WHEN** 管理者が Django Admin のキーワード一覧画面を開く
- **THEN** 各キーワードはキーワードテキストで識別可能な形式で表示される（`__str__()` が `keyword_text` を返す）
