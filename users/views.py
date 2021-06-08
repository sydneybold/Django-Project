from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

# Models
from users.models import Profile
from posts.models import Post

# Forms
from users.forms import SignupForm, UpdateForm


# Create your views here.
class SignupView(generic.CreateView):
    """Signup View."""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        password_confirmation = form.cleaned_data['password_confirmation']
        if password != password_confirmation:
            messages.error(self.request, "Passwords do not match", extra_tags="alert alert-danger")
            return render(self.request, self.template_name, {'form': form})
        user.set_password(password)
        user.save()

        Profile.objects.create(user=user)

        return super(SignupView, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("form is invalid.. this is just an HttpResponse object")

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Hello"""

class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'users/update_profile.html'
    form_class = UpdateForm
    model = Profile

    def get_success_url(self, **kwargs):
        return reverse('users:detail', kwargs={'pk': self.object.user.pk})

class UserDetailView(generic.DetailView):
    model = Profile
    template_name = 'users/detail.html'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user_name = self.get_object()
        user = User.objects.get(username=user_name)
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
