from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import Article

SAMPLE_ARTICLES = [
    {
        "username": "alice",
        "title": "Django入門: モデルとマイグレーション",
        "content": (
            "Djangoのモデル定義からマイグレーション実行までを解説する記事です。"
            "ORMの基本を扱います。"
        ),
        "days_ago": 10,
    },
    {
        "username": "alice",
        "title": "URLとViewの配線を理解する",
        "content": "urls.pyとviews.pyの関係、URLパターンの書き方を丁寧に説明します。",
        "days_ago": 7,
    },
    {
        "username": "alice",
        "title": "テンプレートで記事一覧を表示する",
        "content": "Djangoテンプレート言語を使って記事一覧をレンダリングする方法を紹介します。",
        "days_ago": 4,
    },
    {
        "username": "bob",
        "title": "HTMXで作るインクリメンタル検索",
        "content": (
            "HTMXのhx-get属性とhx-triggerを使い、"
            "ページ全体をリロードせずに検索結果を更新する方法を解説します。"
        ),
        "days_ago": 2,
    },
    {
        "username": "bob",
        "title": "レスポンシブデザインとアクセシビリティの基礎",
        "content": (
            "メディアクエリによるレスポンシブ対応と、"
            "フォーカス表示やコントラスト比などのアクセシビリティ配慮を紹介します。"
        ),
        "days_ago": 1,
    },
]


class Command(BaseCommand):
    help = "Seed the database with sample Article records for search/filter demos."

    def handle(self, *args, **options):
        created_count = 0
        for entry in SAMPLE_ARTICLES:
            author, _ = User.objects.get_or_create(
                username=entry["username"],
                defaults={"password": "unusable"},
            )
            if not author.has_usable_password():
                author.set_unusable_password()
                author.save(update_fields=["password"])

            article, created = Article.objects.get_or_create(
                title=entry["title"],
                defaults={
                    "content": entry["content"],
                    "author": author,
                },
            )
            if created:
                created_at = timezone.now() - timedelta(days=entry["days_ago"])
                Article.objects.filter(pk=article.pk).update(created_at=created_at)
                created_count += 1

        skipped_count = len(SAMPLE_ARTICLES) - created_count
        message = f"Seeded {created_count} new article(s); {skipped_count} already existed."
        self.stdout.write(self.style.SUCCESS(message))
