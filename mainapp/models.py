from django.db import models
from userapp.models import *
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    amount  = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    units = models.CharField(max_length=50)
    income_date = models.DateField(auto_now_add=True, null=True)
    salesman = models.ForeignKey(Salesman, on_delete=models.SET_NULL, null=True)            # FK
    def __str__(self) -> str:
        return f"{self.title}, {self.brand}"

class Client(models.Model):
    name = models.CharField(max_length=30)
    shop_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    debt = models.PositiveSmallIntegerField(default=0)
    salesman = models.ForeignKey(Salesman, on_delete=models.SET_NULL, null=True)            # FK
    def __str__(self) -> str:
        return f"{self.name}, {self.shop_name}({self.address})"