from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/search/', views.article_search, name='article_search'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
