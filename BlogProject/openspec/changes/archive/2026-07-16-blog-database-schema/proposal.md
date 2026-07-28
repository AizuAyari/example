## Why

"The Blogs" アプリに必要なコアデータモデル（ユーザー・記事・キーワード）が存在しないため、ブログ機能を実装できない。Phase 1 でユーザーと記事の基盤を確立し、Phase 2 でキーワードタグ機能を拡張する。

## What Changes

- Django 標準の `django.contrib.auth.models.User`（組み込みモデル）をそのままユーザー管理の基盤として使用する（カスタムモデルへの置き換えは行わない。一意なユーザー名・ハッシュ化パスワードは Django 標準機能でカバーされる）
- `Article` モデルを新規作成する（タイトル・本文・著者外部キー・作成日時・更新日時）
- `Keyword` モデルを新規作成する（Phase 2 オプション）（キーワードテキスト・記事外部キー）
- `blog` アプリ用のデータベースマイグレーションを作成・適用する

## Capabilities

### New Capabilities

- `blog-user`: Django 組み込み User モデルを基盤とした認証・識別機能
- `blog-article`: 記事の CRUD 基盤となるデータモデル
- `blog-keyword`: 記事へのキーワードタグ付け機能（Phase 2）

### Modified Capabilities

<!-- 既存スペックへの要件変更なし -->

## Impact

- `blog/models.py`: `Article`、`Keyword` モデル追加（`User` は Django 組み込みモデルをそのまま使用、変更なし）
- `blog/migrations/`: 初期マイグレーションファイル生成
- `blog/admin.py`: 各モデルの管理画面登録（`Article`、`Keyword`）
