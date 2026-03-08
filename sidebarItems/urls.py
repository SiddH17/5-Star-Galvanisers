from django.urls import path
from . import views

urlpatterns = [
    path('stock-card/', views.stockCard, name='stock-card'),
]
