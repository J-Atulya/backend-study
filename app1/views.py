from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import feature

# Create your views here.
def index(request):
    feat = feature.objects.all()
    return render(request, 'basic.html', {'variables' : feat})

def register(request):
    
    if request.method == 'POST':
        # if the user submits something
        uname = request.POST['username']
        # this stores the value given to textbox username to this variable
        mail = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['password2'] 

        if password == pass2:
            #checking if the email already exists
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username Already Used' )
                return redirect('register')
            
            elif User.objects.filter(email=mail).exists():
                messages.info(request, 'Email Already Used')
                # redirecting back to the refreshed form page with 
                return redirect('register')    
            
            else:
                # if the email and username is not already in use
                user = User.objects.create_user(username=uname, email=mail, password=pass2)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request, 'Password do not match')
            return redirect('register')
    
    else:
        return render(request, 'register.html')

def counter(request):
    words = request.POST['text']
    numWords = len(words.split())
    return render(request, 'countWords.html', { 'numWords' : numWords})


