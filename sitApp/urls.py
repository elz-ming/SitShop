from django.urls import path, include
from . import views
from sitApp import views
urlpatterns = [
    path('', views.home, name='home'),                   # The URL and function to display home page
    path('about/', views.about, name='about'),           # The URL and function to display about page
    path('contact/', views.contact, name='contact'),     # The URL and function to display contacts page
    path('detail', views.detail, name='detail'),
    # retrieve product based on the product_id variable
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'), 
    path('command/<int:id>/<cmd>', views.command, name="command"),
    path('comparison/', views.comparison, name='comparison'),
    # export pdf from comparison page
    path('export_pdf/', views.export_to_pdf, name='export_to_pdf'),

    path('test/', views.test, name='test'),
]


