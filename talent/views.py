from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import TalentProfileForm, ContactTalentForm, TalentImageForm
from .models import TalentProfile


def get_youtube_embed_url(url):
    if not url:
        return None

    if "youtube.com/watch?v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
        return f"https://www.youtube.com/embed/{video_id}"

    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
        return f"https://www.youtube.com/embed/{video_id}"

    if "youtube.com/embed/" in url:
        return url

    return None


@login_required
def create_profile(request):
    if request.user.role != 'talent':
        messages.error(request, "Only talent users can create profiles.")
        return redirect('dashboard')

    profile = TalentProfile.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = TalentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            talent_profile = form.save(commit=False)
            talent_profile.user = request.user
            talent_profile.save()
            messages.success(request, "Profile saved successfully!")
            return redirect("dashboard")
        messages.error(request, "Please fix the errors in the form.")
    else:
        form = TalentProfileForm(instance=profile)

    return render(request, "talent/create_profile.html", {"form": form})


@login_required
def upload_gallery_image(request):
    if request.user.role != 'talent':
        messages.error(request, "Only talent users can upload gallery images.")
        return redirect('dashboard')

    profile = TalentProfile.objects.filter(user=request.user).first()

    if not profile:
        messages.error(request, "Please create your profile first.")
        return redirect('create_profile')

    if request.method == "POST":
        form = TalentImageForm(request.POST, request.FILES)
        if form.is_valid():
            gallery_image = form.save(commit=False)
            gallery_image.talent_profile = profile
            gallery_image.save()
            messages.success(request, "Gallery image uploaded successfully!")
            return redirect('talent_detail', pk=profile.pk)
        messages.error(request, "Please fix the errors.")
    else:
        form = TalentImageForm()

    return render(request, "talent/upload_gallery_image.html", {"form": form})


def talent_list(request):
    q = request.GET.get("q")
    category = request.GET.get("category")
    location = request.GET.get("location")
    experience_level = request.GET.get("experience_level")

    talents = TalentProfile.objects.all()

    if q:
        talents = talents.filter(full_name__icontains=q)

    if category:
        talents = talents.filter(category=category)

    if location:
        talents = talents.filter(location__icontains=location)

    if experience_level:
        talents = talents.filter(experience_level=experience_level)

    return render(request, "talent/talent_list.html", {"talents": talents})


def talent_detail(request, pk):
    talent = get_object_or_404(TalentProfile, pk=pk)
    embed_url = get_youtube_embed_url(talent.video_link)
    gallery_images = talent.gallery_images.all()

    if request.method == "POST":
        if not request.user.is_authenticated or request.user.role != 'coach':
            messages.error(request, "Only coaches can contact talent.")
            return redirect("login")

        contact_form = ContactTalentForm(request.POST)

        if contact_form.is_valid():
            sender_name = contact_form.cleaned_data["sender_name"]
            sender_email = contact_form.cleaned_data["sender_email"]
            subject = contact_form.cleaned_data["subject"]
            message = contact_form.cleaned_data["message"]

            full_message = (
                f"Message for {talent.full_name}\n\n"
                f"From: {sender_name}\n"
                f"Email: {sender_email}\n\n"
                f"{message}"
            )

            recipient_email = talent.user.email

            if recipient_email:
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [recipient_email],
                    fail_silently=False,
                )
                messages.success(request, "Message sent successfully!")
                return redirect("talent_detail", pk=talent.pk)

            messages.error(request, "This talent has no email available.")
    else:
        contact_form = ContactTalentForm()

    return render(
        request,
        "talent/talent_detail.html",
        {
            "talent": talent,
            "contact_form": contact_form,
            "embed_url": embed_url,
            "gallery_images": gallery_images,
        }
    )


@login_required
def like_talent(request, pk):
    if request.method == "POST":
        talent = get_object_or_404(TalentProfile, pk=pk)
        talent.likes += 1
        talent.save()
        messages.success(request, "You liked this talent.")
        return redirect("talent_detail", pk=pk)

    return redirect("talent_list")