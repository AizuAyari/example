from django.conf import settings
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Keyword(models.Model):
    keyword_text = models.CharField(max_length=100)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="keywords",
    )

    def __str__(self):
        return self.keyword_text
