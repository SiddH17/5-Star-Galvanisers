from django.urls import path
from . import views

urlpatterns = [
    path('stock-card/', views.stockCardRender, name='stock-card'),
    path('add-stock-card/', views.addStockCard, name='add-stock-card'),
    path('edit-stock-card/', views.editStockCard, name='edit-stock-card'),
]
