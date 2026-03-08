from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

#Ensures that only logged in users are able to view this page
def home(request):
    #If in case the user is not in the session
    if not request.session.get('user_id'):
        return redirect('login')

    return render(request, 'home.html')