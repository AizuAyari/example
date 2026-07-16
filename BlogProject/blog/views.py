from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ArticleForm, RegisterForm
from .models import Article


def home(request):
    return render(request, "blog/home.html")


def _filter_articles(request):
    articles = Article.objects.all()

    keyword = request.GET.get("q", "").strip()
    if keyword:
        articles = articles.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))

    author_id = request.GET.get("author", "").strip()
    if author_id:
        articles = articles.filter(author_id=author_id)

    date_value = request.GET.get("date", "").strip()
    if date_value:
        articles = articles.filter(created_at__date=date_value)

    return articles


def article_list(request):
    articles = _filter_articles(request)
    authors = User.objects.filter(articles__isnull=False).distinct().order_by("username")
    return render(
        request,
        "blog/article_list.html",
        {"articles": articles, "authors": authors},
    )


def article_search(request):
    articles = _filter_articles(request)
    return render(request, "blog/_article_list_results.html", {"articles": articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "blog/article_detail.html", {"article": article})


@login_required(login_url="login")
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("article_detail", article_id=article.id)
    else:
        form = ArticleForm()
    return render(request, "blog/article_form.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})


@require_POST
def logout_view(request):
    auth_logout(request)
    return redirect("home")
