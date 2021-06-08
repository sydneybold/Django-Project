from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy



# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


class CreatePostView(generic.CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostFeedView(generic.ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'
    ordering = ('-created',)
    paginate_by = 4

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
