from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request,f'Le compte de {username} à été bien crée')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
