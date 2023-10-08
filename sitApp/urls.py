from django.urls import path, include
from . import views
from sitApp import views

urlpatterns = [
    path('', views.home, name='home'),                   # The URL and function to display home page
    path('comparison', views.compare, name='compare'),   # The URL and function to display compare page
    path('welcome/', views.welcome, name='welcome'),      # The URL and function to display welcome page
    path('command/<int:id>/<cmd>', views.command, name="command"),
    path('comparison/', views.compare, name='dropdown_example'),

    
]