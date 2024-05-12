from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from .models import UserInfo
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def my_account_view(request):
    if request.user.is_authenticated:
        account_data = UserInfo.objects.get(user=request.user)
        user = User.objects.get(username=request.user)
        email = user.email
        address = f"{account_data.house_number} {account_data.street}, {account_data.city}, {account_data.country}."
        context = {
            'account_data': account_data,
            'email': email,
            'address': address
        }
        print(account_data.image)
        return render(request, 'my_account.html', context)
    else:
        return redirect('index')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_info = UserInfo.objects.create(user=user)
            user_info.save()
            return redirect('login')
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def account_settings_view(request):
    pass
