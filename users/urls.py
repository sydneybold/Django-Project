from django.urls import path
from django.contrib.auth.decorators import login_required


from users.views import *

app_name = "users"
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('<pk>', login_required(UserDetailView.as_view()), name='detail'),
]
