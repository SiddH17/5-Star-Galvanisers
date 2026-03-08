from django.shortcuts import render


# Create your views here.
def stockCard(request):
    return render(request, 'stockCard.html')

def addStockCard(request):
    return render(request, 'addStockCard.html')

