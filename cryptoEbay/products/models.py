from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    BITCOIN = 'BTC'
    PAYMENT = [(BITCOIN, 'BTC')]
    
    title = models.CharField(max_length=50)
    discription = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    paymet_method = models.CharField(
        max_length=4,
        choices=PAYMENT,
        default=BITCOIN,
    )
    location = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=80)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
