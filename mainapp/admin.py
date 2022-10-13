from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    search_fields = ('title','brand','salesman')
    list_display = ('id', 'title', 'brand', 'salesman')
    list_display_links = ('id','title','brand')

@admin.register(Client)
class ClientAdmin(ModelAdmin):
    search_fields = ('shop_name','name','salesman')
    list_display = ('id', 'name', 'shop_name', 'salesman')
    list_display_links = ('id','shop_name','name')