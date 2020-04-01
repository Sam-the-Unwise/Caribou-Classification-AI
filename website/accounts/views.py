from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import csrf_exempt

from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate



@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'analysis/category.html')
        else:
            messages.error(request, f'Invalid login or password!')
    # else:
        # form = AuthenticationForm()
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('bases-home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def forgot_view(request):
    return render(request, 'accounts/forgot.html')

def reset_view(request):
    return render(request, 'accounts/password_change.html')

def profile_view(request):
    return render(request, 'accounts/profile.html')

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')

def password_change_done(request):
    return render(request, 'accounts/password_change_done.html')

