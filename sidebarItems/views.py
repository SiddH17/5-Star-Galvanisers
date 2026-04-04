from django.shortcuts import render, redirect
from .forms import stockCardForm

# Create your views here.
def stockCardRender(request):
    return render(request, 'stockCard.html')

def addStockCard(request):
    if request.method == 'POST':
        #Helps select the form from the list
        form = stockCardForm(request.POST)

        if form.is_valid():
            opening = form.cleaned_data['opening_stock']

            stock = form.save(commit=False)
            stock.current_stock = opening
            stock.save()
            print(stock, "The current stock")

            return redirect('stock-card')
    else:
        form = stockCardForm()

    return render(request, 'addStockCard.html', {'form': form})

def editStockCard(request):
    return render(request, 'editStockCard.html')

