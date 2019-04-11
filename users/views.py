from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.instance)
        return redirect('posts:home')
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
