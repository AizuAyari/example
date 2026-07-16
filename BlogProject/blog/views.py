from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import RegisterForm


def home(request):
    return render(request, "blog/home.html")


def article_list(request):
    titles = [
        "Django入門: モデルとマイグレーション",
        "URLとViewの配線を理解する",
        "テンプレートで記事一覧を表示する",
    ]
    return render(request, "blog/article_list.html", {"titles": titles})


def article_detail(request, article_id):
    return render(request, "blog/article_detail.html", {"article_id": article_id})


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
