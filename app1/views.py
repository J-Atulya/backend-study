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

def loginpage(request):
    #we got info from login page and we are storing it in variables
    if request.method == 'POST':
        uN = request.POST['un']
        pW = request.POST['pw'] 
        #making the user with the given username and password
        user = auth.authenticate(username = uN, password = pW)
        #checking if the user exists or not-> returns none if user doesnt exist
        if user is not None:
            auth.login(request,user)
            #user is redirected to the home page, which here is basic.html
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            #message is shown in the redirected page which is loginpage
            return redirect ('loginpage')
    
    else:
        return render(request, 'login.html')

#creating a function to redirect from logout
def logout(request):
    #the user is logged out
    auth.logout(request)
    #redirected to the basic page
    return redirect('/')