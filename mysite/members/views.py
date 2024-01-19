from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest


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

