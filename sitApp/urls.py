from django.urls import path, include
from . import views
from sitApp import views
urlpatterns = [
    # The URL to display home page / product listing
    path('', views.home, name='home'),                   
    path('p/', views.home, name='allproduct'),
    
    # The URL to display user listing
    path('u/', views.alluser, name='alluser'),

    # The URL to display comparison of (up to) 4 products
    path('comparison/<str:product_list>/', views.comparison, name='comparison'),

    # export pdf from comparison page
    path('generate_pdf/<str:product_ids>/', views.generate_pdf, name='generate_pdf'),

    # retrieve product based on the product_id variable
    path('p/<str:pid>', views.p_detail, name='p_detail'), 
    
    # retrieve product based on the product_id variable
    path('u/<str:uid>', views.u_detail, name='u_detail'), 

    # The URL and function to display about us page and contact us page
    path('about/', views.about, name='about'),           
    path('contact/', views.contact, name='contact')
]


