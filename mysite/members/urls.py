from django.contrib import admin
from django.urls import path

from . import views

app_name = "members"

urlpatterns = [
        path("login_user/", views.login_user, name="login_user")
]