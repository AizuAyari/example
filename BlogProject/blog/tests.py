from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

from .models import Article, Keyword


class ArticleModelTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="author", password="password123")

    def test_created_at_is_set_automatically(self):
        article = Article.objects.create(title="Title", content="Content", author=self.author)
        self.assertIsNotNone(article.created_at)

    def test_updated_at_changes_on_update_but_created_at_does_not(self):
        article = Article.objects.create(title="Title", content="Content", author=self.author)
        original_created_at = article.created_at
        original_updated_at = article.updated_at

        article.title = "Updated Title"
        article.save()
        article.refresh_from_db()

        self.assertEqual(article.created_at, original_created_at)
        self.assertGreater(article.updated_at, original_updated_at)

    def test_article_requires_author(self):
        with self.assertRaises(IntegrityError):
            Article.objects.create(title="Title", content="Content", author=None)

    def test_deleting_author_cascades_to_articles(self):
        Article.objects.create(title="Title", content="Content", author=self.author)
        self.author.delete()
        self.assertEqual(Article.objects.count(), 0)

    def test_default_ordering_is_newest_first(self):
        first = Article.objects.create(title="First", content="Content", author=self.author)
        second = Article.objects.create(title="Second", content="Content", author=self.author)
        third = Article.objects.create(title="Third", content="Content", author=self.author)

        articles = list(Article.objects.all())

        self.assertEqual(articles, [third, second, first])

    def test_str_returns_title(self):
        article = Article.objects.create(title="My Title", content="Content", author=self.author)
        self.assertEqual(str(article), "My Title")


class KeywordModelTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="author", password="password123")
        self.article = Article.objects.create(title="Title", content="Content", author=self.author)

    def test_keyword_is_linked_to_article(self):
        keyword = Keyword.objects.create(keyword_text="django", article=self.article)
        self.assertEqual(keyword.article, self.article)
        self.assertIn(keyword, self.article.keywords.all())

    def test_deleting_article_cascades_to_keywords(self):
        Keyword.objects.create(keyword_text="django", article=self.article)
        self.article.delete()
        self.assertEqual(Keyword.objects.count(), 0)

    def test_str_returns_keyword_text(self):
        keyword = Keyword.objects.create(keyword_text="django", article=self.article)
        self.assertEqual(str(keyword), "django")
