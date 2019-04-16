from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.


def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('posts:home')
        return redirect('accounts:login')
    else:
        login_form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'login_form': login_form})


def logout(request):
    auth_logout(request)
    return redirect('posts:home')


def create(request):
    pass
