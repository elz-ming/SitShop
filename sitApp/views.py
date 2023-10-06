from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Alenna, work on this more.
# Additionally, look at templates/components/searchbar.html & templates/pages/home.html
def home(request):
    return render(request, "pages/home.html")

# JingYu, work on this more.
# Additionally, look at templates/components/comparison.html
def compare(request):
    return render(request, "pages/comparison.html")


def welcome(request):
    return HttpResponse("Welcome to my app!")


def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = 'YourModel.objects.filter(your_field__icontains=query)'

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