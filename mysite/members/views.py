from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest


def login_user(request: HttpRequest):
    if request.method == "POST":
        print("hello")
        
        try:
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect(request, HttpResponse("Successfull login!"), {})

            messages.success(request, "Ivalid login data")
            return render(request, "authenticate/login_user.html", {})

        except Exception as e:
            return render(request, "authenticate/login_user.html", {"error": e})

    return render(request, "authenticate/login_user.html", {})

