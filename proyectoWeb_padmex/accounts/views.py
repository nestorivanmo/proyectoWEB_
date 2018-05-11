from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.

def login_view(request):
    title = "Login"
    username1 = ""
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username1 = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username1, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "form.html", {"form": form, "title": title, "username":username1})

def register_view(request):
    title = "Register"
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")
    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)

def logout_view(request):
    logout(request)
    return redirect("/")
    return render(request, "form.html", {})