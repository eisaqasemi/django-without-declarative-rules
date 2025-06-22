from django.urls import path

from . import views
from . import auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/login/", auth_views.login_view, name="login"),
    path("api/signup/", auth_views.signup_view, name="signup"),
]