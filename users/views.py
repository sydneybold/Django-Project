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

class SignupView(generic.CreateView):
    # the view to create a user
    template_name = 'users/signup.html'         # set the template name to signup
    form_class = SignupForm                     # set the form where the person can create a user
    success_url = reverse_lazy('users:login')   # set the url that the page will redirect to when the form is submitted

    def form_valid(self, form):
        # function to save the form data
        user = form.save(commit=False)             # get the user
        password = form.cleaned_data['password']   # get the password

        user.set_password(password)                # set the password for the new user
        user.save()                                # save the new user
        Profile.objects.create(user=user)          # create a new profile that is linked to the new user

        return super(SignupView, self).form_valid(form)   # return the saved data

    def form_invalid(self, form):
        # return an HttpResponse if the form is invalid
        return HttpResponse("The form is invalid")

class LoginView(auth_views.LoginView):
    # the view to log a user in
    template_name = 'users/login.html'       # set the template name to login
    redirect_authenticated_user = True       # redirects user if/when authenticated


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    # the view to log a user out
    """ Nothing is needed in this function """

class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'users/update_profile.html'     # set the template name to update
    form_class = UpdateForm               # set the form where the person can update their profile
    model = Profile         # set the model as Profile because that is what is being updated

    def get_success_url(self, **kwargs):
        # returns the url to go to when the form is submitted
        return reverse('users:detail', kwargs={'pk': self.object.user.pk})

class UserDetailView(generic.DetailView):
    # the view to see the profile details
    model = Profile         # set the model as Profile because that is what is being displayed
    template_name = 'users/detail.html'         # set the template name to display the profile details

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        # geth the context
        user_name = self.get_object()           # get the username of the user
        user = User.objects.get(username=user_name) # get the user with that username
        context['user'] = user          # add the user to the context
        context['posts'] = Post.objects.filter(user=user).order_by('-created') # add the user's posts to the context
        return context
