from django.urls import path
from statsapp.views import *

urlpatterns = [
    path('', StatsView.as_view()),
]
