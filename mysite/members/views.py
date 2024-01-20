from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterUserForm


def login_user(request: HttpRequest):
    if request.method == "POST":
        print("hello")
        
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(to="flashcards:index")

            messages.success(request, "Ivalid login data")
            return render(request, "authenticate/login_user.html", {})

        except Exception as e:
            messages.success(request, f"{e}")
            return render(request, "authenticate/login_user.html", {})

    return render(request, "authenticate/login_user.html", {})


def logout_user(request: HttpRequest):
    logout(request)
    messages.info(request, "You were logged out!")
    return redirect(to="flashcards:index")


def register_user(request: HttpRequest):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
        # password = request.POST["password"]
        # check_password = request.POST["check_password"]
        # if password != check_password:
        #     return redirect(to="members:register_user")

        # username = request.POST["username"]
        # email = request.POST["email"]
            messages.success(request, "User registered successfuly")
            return redirect(to="flashcards:index")

        messages.info(request, "The form was filled out incorrectly.")
        return render(request, "authenticate/register_user.html", {"form": form})

    form = RegisterUserForm()
    return render(request, "authenticate/register_user.html", {"form": form})


def new_user(request: HttpRequest):
    return render(request, "authenticate/new_user.html", {})
