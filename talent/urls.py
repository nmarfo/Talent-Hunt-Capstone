from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_profile, name="create_profile"),
    path("gallery/upload/", views.upload_gallery_image, name="upload_gallery_image"),
    path("<int:pk>/like/", views.like_talent, name="like_talent"),
    path("", views.talent_list, name="talent_list"),
    path("<int:pk>/", views.talent_detail, name="talent_detail"),
]