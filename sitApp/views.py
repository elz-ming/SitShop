from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Alenna, work on this more.
# Additionally, look at templates/components/searchbar.html & templates/pages/home.html
def home(request):
    return render(request, "pages/home.html")

# JingYu, work on this more.
# Additionally, look at templates/components/comparison.html
def compare(request):
    return render(request, "pages/comparison.html")