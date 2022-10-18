from django.db import models
from userapp.models import Salesman
from mainapp.models import Product, Client

# Create your models here.

class Statistics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    salesman = models.ForeignKey(Salesman, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveSmallIntegerField(default=1)
    total = models.PositiveSmallIntegerField()
    payed = models.PositiveSmallIntegerField()
    debt = models.PositiveSmallIntegerField(default=0)
    def __str__(self) -> str:
        return f"{self.product} --- {self.salesman}11"
    