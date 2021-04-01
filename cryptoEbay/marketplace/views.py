from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product

class ProductListView(ListView):
   model = Product
   template_name = 'marketplace/home.html'
   context_object_name = 'items'
   
