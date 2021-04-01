from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, 
    DetailView,
    UpdateView,
    DeleteView
)

from .models import Product

class ProductDitailView(DetailView):
    model = Product
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'discription', 'price', 'paymet_method', 'contact_info', 'location']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'discription', 'price', 'paymet_method', 'contact_info', 'location']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        
class ProductDeletelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'
    
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        