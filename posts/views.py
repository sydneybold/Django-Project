from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


class CreatePostView(generic.CreateView):
    # the view to create a post
    template_name = 'posts/new.html'      # set the template name to create a new post
    form_class = PostForm          # set the form where the person can create a post
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        # get the context data
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        # save the data from the form
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostFeedView(generic.ListView):
    # the view to display all the posts in the feed
    model = Post                # set the model as Post
    template_name = 'posts/feed.html'   # set the template to display the feed
    context_object_name = 'posts'    # set the context object name to posts to use in the template
    ordering = ('-created',)        # order the photos from earlier to latest created
    paginate_by = 4             # set the pagination to 4 posts a page

class PostDetailView(generic.DetailView):
    # the view to display a post
    model = Post            # set the model as Post
    template_name = 'posts/detail.html'     # set the template to display the details of the post
