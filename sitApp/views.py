from io import BytesIO
from itertools import product
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, User
from django.db.models import Q
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
import requests
import uuid
import cgi

# Create your views here.


def home(request):
    all_products  = Product.objects.all()
    search_query  = request.GET.get('q')

    if search_query:
        all_products = all_products.filter(product_name__icontains=search_query)

    paginator =  Paginator(all_products, 60)
    
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, "pages/home.html", {'products':products, 'search_query':search_query})


def alluser(request):
    all_users  = User.objects.all()
    search_query  = request.GET.get('q')

    if search_query:
        all_users = all_users.filter(username__icontains=search_query)

    paginator =  Paginator(all_users, 60)
    
    page = request.GET.get('page')
    users = paginator.get_page(page)

    return render(request, "pages/alluser.html", {'users':users, 'search_query':search_query})


def comparison(request, product_list=None):
    products = product_list.split(',')
    products = [Product.objects.get(product_id=x) for x in products]

    return render(request, "pages/comparison.html", {'products':products, 'product_list':product_list})

def generate_pdf(request, product_ids=None):
    products = product_ids.split(',')
    products = [Product.objects.get(product_id=x) for x in products]

    context = {
      'products':products,
      'product_list':product_ids
    }

    template = get_template('pages/expComparison.html')

    html = template.render(context)

    pdf_data = BytesIO()

    pdf_page_options = {"orientation": "Landscape"}

    pisa_status = pisa.CreatePDF(
        html,
        dest=pdf_data,
        media_css=True,
        pagesize="A4",
        pdf_page_options=pdf_page_options,
        show_error_as_pdf=True
    )

    if not pisa_status.err:
        response = HttpResponse(pdf_data.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="comparison.pdf"'    
        pdf_data.close()
        return response
    else:
        return HttpResponse('gg')


def p_detail(request, pid):
    product = get_object_or_404(Product, product_id=pid)
    return render(request, 'pages/detail.html', {'product': product})


def u_detail(request, uid):
    user = get_object_or_404(User, username=uid)
    return render(request, 'pages/userdetail.html', {'user': user})


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")


# End views.