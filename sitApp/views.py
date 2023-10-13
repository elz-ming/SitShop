from io import BytesIO
from itertools import product
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.db.models import Q
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
import requests
import uuid
import cgi

challenge = uuid.uuid4().hex
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





# def comparison(request):
#     return render(request, "pages/comparison.html", context={"cards": cards})

def product_comparison_table(request):
    products = Product.objects.all()
    return render(request, 'pages/test.html', {'products': products})

def test(request):
    return render(request, "pages/test.html")

def form_view(request):
  # Validate the form
  if contact.is_valid():
    # Redirect the user to the challenge response test view
    return HttpResponseRedirect('/challenge_response_test')

  # Display the form again
  return render(request, 'contact.html', {'contact':contact})


def challenge_response_test_view(request):
  # Generate a random challenge
  challenge = uuid.uuid4().hex
  # Save the challenge in the session
  request.session['challenge'] = challenge
  # Get the user's response
  response = request.POST.get('response')
   # If the response is correct, allow the user to submit the form
  if response == challenge:
    # Process the form submission
    return HttpResponseRedirect('/success')
   # Otherwise, display an error message
  return render(request, 'error.html', message='Challenge-response test failed.')


def verify_challenge_response(request):
  # Get the challenge from the session
  challenge = request.session.get('challenge')

  # Get the user's response
  response = request.POST.get('response')

  # If the response is correct, allow the user to submit the form
  if response == challenge:
    return HttpResponseRedirect('/success')

  # Otherwise, display an error message
  return render(request, 'pages/error.html', message='Challenge-response test failed.')

def contact_form_view(request):
  # Validate the form
  if contact.is_valid():
    # Redirect the user to the challenge response test view
    return HttpResponseRedirect('/challenge_response_test')

  # Display the form again
  return render(request, 'contact_form.html', {'contact': contact})


#   if not request.form.get('not_a_bot'):
#     return render(request, 'error.html', message='You must agree that you are not a bot to proceed.')

#   # Verify that the user is human using a CAPTCHA service

#   # If the CAPTCHA verification is successful, allow the user to proceed
#   return HttpResponseRedirect('/success')

#   # Otherwise, display an error message and prevent the user from proceeding
#   return render(request, 'error.html', message='CAPTCHA verification failed.')

# def verify_captcha(captcha_response):
#   # Replace this with the URL of your CAPTCHA service
#   captcha_url = 'https://example.com/captcha/verify'

#   # Replace this with your CAPTCHA service's API key
#   captcha_api_key = 'YOUR_API_KEY'

#   response = requests.post(captcha_url, data={
#     'response': captcha_response,
#     'api_key': captcha_api_key
#   })

#   if response.status_code == 200:
#     return response.json()['success']
#   else:
#     return False
  
def userdetail(request):
    return render(request, "pages/userdetail.html")

def alluser(request):
    return render(request, "pages/alluser.html")