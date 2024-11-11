from django.urls import path
from .views import PostCreateView, PostDeleteView, PostUpdateView, ProfileEditView, PostEditView
from . import views
from .views import become_author

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news/search/', views.news_search, name='news_search'),
    path('news/create/', PostCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', PostDeleteView.as_view(), name='news_delete'),
    path('articles/create/', PostCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', PostUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', PostDeleteView.as_view(), name='article_delete'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('become_author/', become_author, name='become_author'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),




]
