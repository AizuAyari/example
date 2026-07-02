from django.http import HttpResponse


def home(request):
    return HttpResponse("The Blogs へようこそ！")


def article_list(request):
    titles = [
        "Django入門: モデルとマイグレーション",
        "URLとViewの配線を理解する",
        "テンプレートで記事一覧を表示する",
    ]
    return HttpResponse("<br>".join(titles))


def article_detail(request, article_id):
    return HttpResponse(f"記事ID: {article_id} の詳細表示")
