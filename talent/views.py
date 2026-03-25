from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import TalentProfileForm
from .models import TalentProfile


@login_required
def create_profile(request):
    profile = TalentProfile.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = TalentProfileForm(request.POST, instance=profile)
        if form.is_valid():
            talent_profile = form.save(commit=False)
            talent_profile.user = request.user
            talent_profile.save()
            return redirect("dashboard")
    else:
        form = TalentProfileForm(instance=profile)

    return render(request, "talent/create_profile.html", {"form": form})