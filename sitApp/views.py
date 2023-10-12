from itertools import product
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa
import cgi

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

    return render(request, "pages/home.html", {'products':products, 'search_query':search_query})

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")

# JingYu, work on this more.
# Additionally, look at templates/components/comparison.html
def comparison(request, product_list=None):
    products = product_list.split(',')
    products = [Product.objects.get(product_id=x) for x in products]

    return render(request, "pages/comparison.html", {'products':products})

# JingYu, work on this more.
# Additionally, look at templates/components/comparison.html

def detail(request, pid):
    product = get_object_or_404(Product, product_id=pid)
    return render(request, 'pages/detail.html', {'product': product})

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
def search(request):
    # defines what happens when there is a GET request

    if request.method == "GET":
        title = request.GET.get("q")
        return render(request, 'pages/home.html')
    # defines what happens when there is a POST request
    else:
        return render(request, 'pages/home.html')

def cards_view(request):
    # Your view logic goes here if needed
    return render(request, 'pages/cards.html')

def product_comparison_table(request):
    products = Product.objects.all()
    return render(request, 'pages/test.html', {'products': products})

def test(request):
    return render(request, "pages/test.html")