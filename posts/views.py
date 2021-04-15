from django.shortcuts import render
from django.views import generic

# Models
from posts.models import Post


# change to generic.CreateView
class CreatePostView(generic.ListView):
    template_name = 'posts/new.html'
    # form_class = PostForm
    context_object_name = 'form'

    def get_queryset(self):
        return Post.objects


class PostFeedView(generic.ListView):
    template_name = 'posts/feed.html'
    model = Post
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    template_name = 'posts/detail.html'
    slug_field = 'title'
    slug_url_kwarg = 'post_title'
    queryset = Post.objects.all()
    context_object_name = 'post'
