from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accounts.forms import RegisterForm, LoginForm
from accounts.utils import create_customer


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', context={'form': LoginForm()})

    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        cd = login_form.cleaned_data
        username, password = cd['username'], cd['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages.error(request, 'invalid login/password')
    else:
        messages.error(request, login_form.errors_prettified)
    return redirect('login')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html', context={'form': RegisterForm()})

    register_form = RegisterForm(request.POST)
    if register_form.is_valid():
        new_user = register_form.save(commit=False)
        cd = register_form.cleaned_data
        new_user.set_password(cd['password'])
        new_user.save()
        create_customer(new_user, cd['phone_number'])
        login(request, new_user)
        return redirect('main_page')
    messages.error(request, register_form.errors_prettified)
    return redirect('register')


def logout_view(request):
    logout(request)
    return redirect('main_page')
