from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product

from .forms import ProductCreation

@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        form = ProductCreation(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            item = form.cleaned_data.get('title')
            messages.success(request, f'Product with title - {item} has been created')
            return redirect('home-page')
    else:
        form = ProductCreation()
        
    return render(request, 'products/create.html', {'form': form, 'title': 'Sell a new product'})
            
