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
    path('userdetail/<str:userid>', views.userdetail, name='userdetail'),
    path('test/', views.test, name='test'),
    path('challenge_response_test_view', views.challenge_response_test_view, name='challenge_response_test_view'),
    path('verify_challenge_response', views.verify_challenge_response, name='verify_challenge_response'),
    path('form_view', views.form_view, name='form_view'),
    path('alluser/', views.alluser, name='alluser'),
]


