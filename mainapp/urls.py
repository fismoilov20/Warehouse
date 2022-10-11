from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', SectionsView.as_view()),
    path('products', ProductsView.as_view(), name='products'),
    path('clients', ClientsView.as_view(), name='clients'),

]
