from io import BytesIO
from itertools import product
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.db.models import Q
from django.template.loader import get_template, render_to_string
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

def detail(request, pid):
    product = get_object_or_404(Product, product_id=pid)
    return render(request, 'pages/detail.html', {'product': product})

def render_to_pdf(request, context):
    html_content = render_to_string('pages/comparison.html', context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

def generate_pdf(request, product_ids):
    # Split the product_ids string into a list of individual IDs
    product_ids = product_ids.split(',')

    # Retrieve products from the database based on the provided product_ids
    products = [Product.objects.get(product_id=product_id) for product_id in product_ids]

    # Convert queryset to a list of dictionaries
    products_data = [{'product_id': product.product_id,
                      'category': product.category,
                      'product_name': product.product_name,
                      'avg_rating': product.avg_rating,
                      'total_rating': product.total_rating,
                      'total_sold': product.total_sold,
                      'price': product.price,
                      'fav_count': product.fav_count,
                      'qty_avail': product.qty_avail,
                      'description': product.description,
                      'img_src': product.img_src} for product in products]

    context = {'products': products_data}

    # Generate PDF
    pdf = render_to_pdf(request, context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "comparison.pdf"
        content = "attachment; filename=%s" % filename
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Error generating PDF", status=400)



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