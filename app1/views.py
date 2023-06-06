from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import feature

# Create your views here.
def index(request):
    feat = feature.objects.all()
    return render(request, 'basic.html', {'variables' : feat})

def register(request):
    
    if request.method == 'POST':
        # if the user submits something
        username = request.POST['username']
        # this stores the value given to textbox username to this variable
        mail = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['password2'] 

        if password == pass2:
            #checking if the email already exists
            if User.objects.filter(email='mail').exists():
                messages.info(request, 'Email Already Used')
                # redirecting back to the refreshed form page with 
                return redirect('register')        


    return render(request, 'register.html')

def counter(request):
    words = request.POST['text']
    numWords = len(words.split())
    return render(request, 'countWords.html', { 'numWords' : numWords})


