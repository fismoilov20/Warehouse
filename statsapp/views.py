from django.shortcuts import render, redirect
from django.views import View
from .models import *


class StatsView(View):
    def get(self, request):
        word = request.GET.get('search')
        stats = Statistics.objects.filter(salesman__user=request.user)
        if word is not None:
            stats = stats.filter(
                product__title__contains=word) | stats.filter(
                product__brand__contains=word) | stats.filter(
                client__shop_name__contains=word) | stats.filter(
                client__name__contains=word
            )    

        data = {
            'stats': stats,
            'products': Product.objects.all(),
            'clients': Client.objects.all(),
            'salesmen': Salesman.objects.all()
        }
        return render(request, 'stats.html', data)

    def post(self, request):
        Statistics.objects.create(
            product=Product.objects.get(id=request.POST.get('product')),
            client=Client.objects.get(id=request.POST.get('client')),
            salesman=Salesman.objects.get(user=request.user),
            amount=request.POST.get('amount'),
            total=request.POST.get('total'),
            debt=request.POST.get('debt'),
            payed=request.POST.get('payed'),
        )
        clt = Client.objects.get(id=request.POST.get('client'))
        clt.debt += int(request.POST.get('debt'))
        clt.save()

        amt = Product.objects.get(id=request.POST.get('product'))
        amt.amount -= int(request.POST.get('amount'))
        amt.save()

        return redirect("/stats")
