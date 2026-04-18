from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('search-talent/', views.search_talent_view, name='search_talent'),
    path('messages/', views.messages_view, name='messages'),
    path('contact/', views.contact_view, name='contact'),
    path('terms/', views.terms_view, name='terms'),
]