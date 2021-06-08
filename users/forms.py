"""Users forms"""

# Django
from django import forms

# Models
from users.models import Profile
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    username = forms.CharField(label='Username', min_length=5, max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password', min_length=8, max_length=15, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_confirmation = forms.CharField(label='Password Confirmation', min_length=8, max_length=15, widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
    first_name = forms.CharField(label='First Name', min_length=2, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', min_length=2, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label='Email', min_length=5, max_length=20, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
    	model = User
    	fields = ['username', 'password', 'password_confirmation', 'first_name', 'last_name', "email"]


class UpdateForm(forms.ModelForm):
    class Meta:
    	model = Profile
    	fields = ['website', 'biography', 'phone_number', 'picture']
