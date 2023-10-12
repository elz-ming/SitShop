from itertools import product
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa
import requests
import uuid
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
  


