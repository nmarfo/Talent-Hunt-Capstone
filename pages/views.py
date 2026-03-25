from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from talent.models import TalentProfile


def home_view(request):
    return render(request, 'pages/home.html')


def about_view(request):
    return render(request, 'pages/about.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'pages/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'pages/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard_view(request):
    return render(request, 'pages/dashboard.html')


def search_talent_view(request):
    category = request.GET.get('category')

    if category:
        talents = TalentProfile.objects.filter(category=category)
    else:
        talents = TalentProfile.objects.all()

    return render(
        request,
        'pages/search_talent.html',
        {'talents': talents}
    )


def messages_view(request):
    return render(request, 'pages/messages.html')


def contact_view(request):
    return render(request, 'pages/contact.html')