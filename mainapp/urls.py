from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', SectionsView.as_view()),
    path('products/', ProductsView.as_view(), name='products'),
    path('clients', ClientsView.as_view(), name='clients'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view()),
    path('clients/delete/<int:pk>', ClientDeleteView.as_view()),
    path('clients/edit/<int:pk>', ClientUpdateView.as_view()),

]
