from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request,f'Le compte de {username} à été bien crée')
            return redirect('article')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
