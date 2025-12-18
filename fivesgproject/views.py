from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

#Ensures that only logged in users are able to view this page
@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')