from django.forms import ModelForm

from .models import Product

class ProductCreation(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'discription', 'price', 'paymet_method', 'contact_info','location']