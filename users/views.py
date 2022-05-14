from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required(redirect_field_name='login')
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/profile.html')