from django.urls import path, include
from . import views
from sitApp import views
urlpatterns = [
    path('', views.home, name='home'),                   # The URL and function to display home page
    path('about/', views.about, name='about'),           # The URL and function to display about page
    path('contact/', views.contact, name='contact'),     # The URL and function to display contacts page
    # retrieve product based on the product_id variable
    path('detail/<str:pid>/', views.detail, name='detail'), 
    path('comparison/<str:product_list>', views.comparison, name='comparison'),
    # export pdf from comparison page
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]


