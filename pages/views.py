from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm, ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Account created successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'pages/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Login successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'pages/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Message from: {name}\nEmail: {email}\n\n{message}"

            send_mail(
                subject,
                full_message,
                email,
                ['djakipat@gmail.com'],  
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

def terms_view(request):
    return render(request, 'pages/terms.html')