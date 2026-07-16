from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

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


class RegisterViewTests(TestCase):
    def test_valid_registration_creates_user_and_logs_in(self):
        response = self.client.post(
            reverse("register"),
            {"username": "newuser", "password1": "StrongPass!2026", "password2": "StrongPass!2026"},
        )

        self.assertRedirects(response, reverse("home"))
        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertIn("_auth_user_id", self.client.session)

    def test_password_mismatch_does_not_create_user(self):
        response = self.client.post(
            reverse("register"),
            {"username": "newuser", "password1": "StrongPass!2026", "password2": "DifferentPass!2026"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="newuser").exists())
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_duplicate_username_does_not_create_second_user(self):
        User.objects.create_user(username="existinguser", password="password123")

        response = self.client.post(
            reverse("register"),
            {"username": "existinguser", "password1": "StrongPass!2026", "password2": "StrongPass!2026"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(username="existinguser").count(), 1)

    def test_get_request_renders_empty_form(self):
        response = self.client.get(reverse("register"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<form")


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="CorrectPass!2026")

    def test_valid_credentials_log_in_and_redirect(self):
        response = self.client.post(
            reverse("login"),
            {"username": "testuser", "password": "CorrectPass!2026"},
        )

        self.assertRedirects(response, reverse("home"))
        self.assertIn("_auth_user_id", self.client.session)

    def test_invalid_password_does_not_log_in(self):
        response = self.client.post(
            reverse("login"),
            {"username": "testuser", "password": "WrongPass!2026"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_nonexistent_user_does_not_log_in(self):
        response = self.client.post(
            reverse("login"),
            {"username": "nouser", "password": "WhoKnows!2026"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotIn("_auth_user_id", self.client.session)


class LogoutViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="CorrectPass!2026")

    def test_post_while_logged_in_logs_out_and_redirects(self):
        self.client.login(username="testuser", password="CorrectPass!2026")

        response = self.client.post(reverse("logout"))

        self.assertRedirects(response, reverse("home"))
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_get_request_is_not_allowed(self):
        self.client.login(username="testuser", password="CorrectPass!2026")

        response = self.client.get(reverse("logout"))

        self.assertEqual(response.status_code, 405)
        self.assertIn("_auth_user_id", self.client.session)

    def test_logout_while_not_logged_in_still_redirects(self):
        response = self.client.post(reverse("logout"))

        self.assertRedirects(response, reverse("home"))
