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
        
    
    def post(self, request):
        Product.objects.create(
            title=request.POST.get('pr_name'),
            brand=request.POST.get('pr_brand'),
            quantity=request.POST.get('pr_amount'),
            price=request.POST.get('pr_price'),
            units=request.POST.get('pr_units'),
            salesman=Salesman.objects.filter(user=request.user).first()
        )
        return redirect('/products/')

class ClientsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'clients': Client.objects.filter(salesman__user=request.user)
            }
            return render(request, 'clients.html', data)
        else:
            return redirect('/login')

class ProductDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            a = Product.objects.get(id=pk)   #  ⬇  # Verifying if the salesman of this id=pk product is request.user   Why?
            if a.salesman == Salesman.objects.get(user=request.user) and request.user.is_staff:   ## In order to Prevent link delete
                a.delete()
            return redirect('/products')
        return redirect('login')         ## name='login'

class ClientDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            a = Client.objects.get(id=pk)   #  ⬇⬇  # Verifying if the salesman of this id=pk product is th current user (request.user)   Why?
            if a.salesman == Salesman.objects.get(user=request.user) and request.user.is_staff:   ## In order to Prevent link delete
                a.delete()
            return redirect('/clients')
        return redirect('login')         ## name='login'

class ClientUpdateView(View):
    def get(self, request, pk):
        data = {
            'client': Client.objects.get(id=pk),
        }
        return render(request, 'client_update.html', data)

    def post(self, request, pk):
        if request.user.is_authenticated:
            a = Client.objects.get(id=pk)
            if Salesman.objects.get(user=request.user) == a.salesman and request.user.is_staff:     ## No link edits!!!
                Client.objects.filter(id=pk).update(
                    name=request.POST.get('client_name'),
                    shop_name=request.POST.get('client_shop'),
                    phone=request.POST.get('client_phone'),
                    address=request.POST.get('client_address'),
                )
            return redirect('/clients')
        return redirect('login')        ## name='login'