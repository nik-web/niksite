from django.urls import path
from base import views

# URL configuration for base
# Add the app_name ("base") to set the app namespace
app_name = "base"

urlpatterns = [
    path('', views.home, name='home'),
    path('impressum/', views.imprint, name='imprint'),
    path('datenschutzrichtlinien/', views.privacy_policy, name='privacy-policy'),
]
