from itertools import product
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Product
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

# Alenna, work on this more.
# Additionally, look at templates/components/searchbar.html & templates/pages
def home(request):
    all_products  = Product.objects.all()
    search_query  = request.GET.get('q')

    if search_query:
        all_products = all_products.filter(product_name__icontains=search_query)

    paginator =  Paginator(all_products, 60)
    
    page = request.GET.get('page')
    products = paginator.get_page(page)
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     #data = Data.objects.filter(first_name__icontains=q)
    #     multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
    #     data = Data.objects.filter(multiple_q)
    # else:
    #     data = Data.objects.all()
    # context = {
    #     'data': data
    # }
    return render(request, "pages/home.html", {'products':products, 'search_query':search_query})

def comparison(request, product_list=None):
    return render(request, "pages/comparison.html")

# JingYu, work on this more.
# Additionally, look at templates/components/comparison.html
def detail(request):
    return render(request, "pages/detail.html")


# When we get the product id
def product_detail(request, product_id):
    # Your logic to retrieve product details based on product_id
    return render(request, 'detail.html', {'product': product})

# Export comparison page to pdf
def export_to_pdf(request, pisa=None):
    # Replace 'comparison.html' with your HTML template's path
    template_path = 'pages/test.html'
    context = {}  # Add any context data needed for rendering the template

    # Create a Django response object with PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="comparison.pdf"'

    # Find the template and render it to the response
    template = get_template(template_path)
    html = template.render(context)

    # Create a PDF from the rendered HTML
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response



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

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")


def cards_view(request):
    # Your view logic goes here if needed
    return render(request, 'pages/cards.html')

import cgi








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



def comparison(request):
    return render(request, "pages/comparison.html", context={"cards": cards})

def product_comparison_table(request):
    products = Product.objects.all()
    return render(request, 'pages/test.html', {'products': products})

def command(request, id, cmd):
    for card in cards:
        if id == card["id"]:
            if cmd == "delete":
                cards.remove(card)
            if cmd == "color":
                colors = ["red", "blue", "green", "silver", "brown"]
                card["color"] = colors[(colors.index(card["color"]) + 1) % len(colors)]
    return redirect("/")


def test(request):
    return render(request, "pages/test.html")


