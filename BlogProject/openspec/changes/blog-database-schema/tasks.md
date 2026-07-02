## 1. モデル定義

- [x] 1.1 `blog/models.py` に `Article` モデルを追加する（`title`, `content`, `author`（`User` への `ForeignKey`, `on_delete=models.CASCADE`）, `created_at`（`auto_now_add=True`）, `updated_at`（`auto_now=True`））
- [x] 1.2 `Article` に `Meta.ordering = ["-created_at"]` を設定し、デフォルトで新しい順に取得されるようにする
- [x] 1.3 `Article.__str__()` を実装し、タイトルを返すようにする
- [x] 1.4 `blog/models.py` に `Keyword` モデルを追加する（`keyword_text`, `article`（`Article` への `ForeignKey`, `on_delete=models.CASCADE`））
- [x] 1.5 `Keyword.__str__()` を実装し、`keyword_text` を返すようにする

## 2. マイグレーション

- [x] 2.1 `python manage.py makemigrations blog` を実行し初期マイグレーションを生成する
- [x] 2.2 生成されたマイグレーションファイルの内容（フィールド定義・外部キーの `on_delete` 挙動）を確認する
- [x] 2.3 `python manage.py migrate` をローカル開発データベースに適用する

## 3. 管理画面登録

- [x] 3.1 `blog/admin.py` に `Article` を `admin.site.register()`（または `@admin.register`）で登録する
- [x] 3.2 `blog/admin.py` に `Keyword` を `admin.site.register()`（または `@admin.register`）で登録する

## 4. テスト

- [x] 4.1 `Article` 作成時に `created_at` が自動設定されることを検証するテストを追加する
- [x] 4.2 `Article` 更新時に `updated_at` が更新され `created_at` は変化しないことを検証するテストを追加する
- [x] 4.3 `author` 未指定では `Article` を保存できないことを検証するテストを追加する
- [x] 4.4 著者ユーザー削除時に紐づく `Article` が連鎖削除されることを検証するテストを追加する
- [x] 4.5 `Article.objects.all()` がデフォルトで `created_at` 降順（新しい順）で返ることを検証するテストを追加する
- [x] 4.6 `Article` の `__str__()` がタイトルを返すことを検証するテストを追加する
- [x] 4.7 `Keyword` が `Article` に正しく紐づいて保存されることを検証するテストを追加する
- [x] 4.8 記事削除時に紐づく `Keyword` が連鎖削除されることを検証するテストを追加する
- [x] 4.9 `Keyword` の `__str__()` が `keyword_text` を返すことを検証するテストを追加する
- [x] 4.10 `pytest` を実行し、全テスト（新規・既存）がパスすることを確認する
