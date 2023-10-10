from django.urls import path, include
from . import views
from sitApp import views

urlpatterns = [
    path('', views.home, name='home'),                   # The URL and function to display home page
    path('about/', views.about, name='about'),           # The URL and function to display about page
<<<<<<< HEAD
    path('contact/', views.contact, name='contact'),     # The URL and function to display contacts page
    path('detail', views.detail, name='detail'),
    path('comparison/', views.compare, name='dropdown_example'),

]





=======
    path('contact/', views.contact, name='contact'),      # The URL and function to display contacts page

    path('comparison/', views.compare, name='dropdown_example'),   # The URL and function to display compare page
    path('detail/', views.detail, name='detail'),
    path('cards/', views.cards_view, name='cards'),      # The URL and function to display popular items
    path('command/<int:id>/<cmd>/', views.command, name="command"),
]
>>>>>>> 5142655847effa8c81815c7b7cbfca30788aefb2
