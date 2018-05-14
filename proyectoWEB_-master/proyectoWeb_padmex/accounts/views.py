from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.mail import EmailMessage
from . import forms


# Create your views here -> VA!

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # create a new user for us
            # log the user in
            login(request, user)
            return redirect('padmex:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('padmex:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('padmex:index')

def recuperar_view(request):
    if request.method == 'POST':
        form = forms.EnviarCorreo(request.POST)
        if form.is_valid():
            email = EmailMessage('Contraseña de PADMEX ', 'Esta es tu contraseña: adsfa123',
                                 'nestor.martinez.98@hotmail.com')
            email.send()
            return redirect('padmex:index')
    else:
        form = forms.EnviarCorreo()
    return render(request, 'accounts/recuperar.html', {'form': form})