from django.urls import path

from posts.views import *

app_name = "posts"
urlpatterns = [
    path('', PostFeedView.as_view(), name='feed'),
    path('posts/new/', CreatePostView.as_view(), name='create_post'),
    path('posts/<pk>/', PostDetailView.as_view(), name='detail'),
]
