from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.PostFeedView.as_view(), name='feed'),
    path('posts/new/', views.CreatePostView.as_view(), name='create_post'),
    path('posts/<slug:post_title>/', views.PostDetailView.as_view(), name='detail'),
]
