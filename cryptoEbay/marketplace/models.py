from django.db import models

from datetime import date

class CoinPriseModel(models.Model):
    name = models.CharField(max_length=8)
    price = models.IntegerField()
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name