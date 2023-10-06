from django.shortcuts import render
from django.http import HttpResponse, request

from home.models import YourModel


# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')
    #return HttpResponse('Hello, welcome to the index page.')
def welcome(request):
    return HttpResponse("Welcome to my app!")


def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = YourModel.objects.filter(your_field__icontains=query)

    return render(request, 'your_template.html', {'results': results})
    # Rest of the view code

'''
the search bar in views.py
<div class="input-group">
          <span class="input-group-text text-body"><i class="fas fa-search" aria-hidden="true"></i></span>
          <input type="text" class="form-control" placeholder="Type here...">
        </div>
      </div>

'''


def home():
    return render(request, 'pages/index.html')