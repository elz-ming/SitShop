from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Data
from .models import Product
from django.db.models import Q
from django.template.loader import get_template


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
def detail(request):
    return render(request, "pages/detail.html")


# When we get the product id
def product_detail(request, product_id):
    # Your logic to retrieve product details based on product_id
    return render(request, 'detail.html', {'product': product})

# Export comparison page to pdf
def export_to_pdf(request):
    # Replace 'comparison.html' with your HTML template's path
    template_path = 'pages/comparison.html'
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

cards = [
    {
        "id": 1,
        "name": "Mercedes A Class",
        "image": "https://i.auto-bild.de/mdb/extra_large/62/aklasse-bb5.png",
        "description": "This is a Mercedess A-Class from autobild.de website.",
        "color": "silver",
    },
    {
        "id": 2,
        "name": "Audi A1",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "This is an Audi A1 from autobild.de website.",
        "color": "brown",
    },
    {
        "id": 3,
        "name": "BMW 2er Gran Tourer",
        "image": "https://down-sg.img.susercontent.com/file/sg-11134201-22110-cc3ayii6f2jv4c",
        "description": "This is a beautiful BMW from autobild.de website.",
        "color": "blue",
    },
    {
        "id": 4,
        "name": "BMW 2er Gran Tourer",
        "image": "https://down-sg.img.susercontent.com/file/sg-11134201-22110-cc3ayii6f2jv4c",
        "description": "This is a beautiful BMW from autobild.de website.",
        "color": "blue",
    },
]


def comparison(request):
    return render(request, "pages/comparison.html", context={"cards": cards})


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

def product_comparison_table(request):
    products = Product.objects.all()
    return render(request, 'pages/test.html', {'products': products})

