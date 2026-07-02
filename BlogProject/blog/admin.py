from django.contrib import admin

from .models import Article, Keyword

admin.site.register(Article)
admin.site.register(Keyword)
