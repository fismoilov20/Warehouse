from django.shortcuts import render, redirect
from django.views import View
from mainapp.models import *
from userapp.models import *
# Create your views here.

class SectionsView(View):
    def get(self, request):
        return render(request, 'sections.html')

class ProductsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'products': Product.objects.filter(salesman__user=request.user)
            }
            return render(request, 'products.html', data)
        else:
            return redirect('/login')

class ClientsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'clients': Client.objects.filter(salesman__user=request.user)
            }
            return render(request, 'clients.html', data)
        else:
            return redirect('/login')

