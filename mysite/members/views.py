from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest


def login_user(request: HttpRequest):
    if request.method == "POST":
        pass
    else:
        ...

    return render(request, "authenticate/login.html", {})
