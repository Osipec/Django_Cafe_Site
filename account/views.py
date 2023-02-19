from django.shortcuts import render, redirect
from .forms import UserRegistration, UserLogin
from django.contrib.auth import login, authenticate, logout

def registration_view(request):
    form = UserRegistration(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password_1'])
        new_user.save()
        return render(request, 'registration_done.html', context={'user': new_user})

    return render(request, 'registration.html', context={'form': form})

def login_view(request):
    form = UserLogin(request.POST or None)
    next_get = request.GET.get('next')

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password_1')
        user = authenticate(username=username, password=password)
        login(request, user)
        next_post = request.POST.get('next')

        return redirect(next_get or next_post or '/')

    return render(request, 'login.html', context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

