from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                auth_login(request, login_form.get_user())
                return redirect('posts:home')
            return redirect('accounts:login')
        else:
            login_form = AuthenticationForm()
            return render(request, 'accounts/login.html', {'login_form': login_form})
    return redirect('posts:home')


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('posts:home')


def create(request):
    if request.method == "POST":
        creation_form = CustomUserCreationForm(request.POST)
        if creation_form.is_valid():
            user = creation_form.save()
            auth_login(request, user)
            return redirect('posts:home')
        return redirect('accounts:create')
    else:
        creation_form = CustomUserCreationForm()
        return render(request, 'accounts/create.html', {'creation_form': creation_form})


def update(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
            if user_change_form.is_valid():
                user_change_form.save()
                return redirect('posts:home')
            return redirect('accounts:update')
        else:
            user_change_form = CustomUserChangeForm(instance=request.user)
            context = {
                'user_change_form': user_change_form,
            }
            return render(request, 'accounts/update.html', context)
    return redirect('accounts:login')
