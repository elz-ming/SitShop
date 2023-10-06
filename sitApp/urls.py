from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),                  # The URL and function to display homepage
    path('comparison', views.compare, name='compare')   # The URL and function to display compare page
]