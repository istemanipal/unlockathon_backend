from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomLoginForm
from . import views

app_name="user"

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path("login",LoginView.as_view(template_name='user/login.html',form_class=CustomLoginForm),name="login"),
    path("logout",LogoutView.as_view(template_name="user/index.html"),name="logout"),
]