from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Salesman(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)            # FK
    task = models.CharField(max_length=40, blank=True)
    def __str__(self) -> str:
        return f"{self.name}, {self.title}({self.address})"