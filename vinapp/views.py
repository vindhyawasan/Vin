from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product

def index(request):
    prds = Product.get_all_products()
    return render(request, 'index.html',{'products': prds})

# Create your views here.
