from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Data
from django.db.models import Q

# Create your views here.

# Alenna, work on this more.
# Additionally, look at templates/components/searchbar.html & templates/pages
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        #data = Data.objects.filter(first_name__icontains=q)
        multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        data = Data.objects.filter(multiple_q)
    else:
        data = Data.objects.all()
    context = {
        'data': data
    }
    return render(request, "pages/home.html", context)


# JingYu, work on this more.
# Additionally, look at templates/components/comparison.html



def welcome(request):
    return HttpResponse("Welcome to my app!")


def search(request):
    # defines what happens when there is a GET request

    if request.method == "GET":
        title = request.GET.get("q")
        return render(request, 'pages/home.html')
    # defines what happens when there is a POST request
    else:
        return render(request, 'pages/home.html')



def compare(request):
    return render(request, "pages/comparison.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")


def cards_view(request):
    # Your view logic goes here if needed
    return render(request, 'pages/cards.html')








'''
def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = 'YourModel.objects.filter(your_field__icontains=query)'

    return render(request, 'base.html', {'results': results})
    # Rest of the view code
'''

'''
the search bar in views.py
<div class="input-group">
          <span class="input-group-text text-body"><i class="fas fa-search" aria-hidden="true"></i></span>
          <input type="text" class="form-control" placeholder="Type here...">
        </div>
      </div>

'''



