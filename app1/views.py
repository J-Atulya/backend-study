from django.shortcuts import render
from django.http import HttpResponse
from .models import feature

# Create your views here.
def index(request):
    feat = feature.objects.all()
    return render(request, 'basic.html', {'variables' : feat})

def register(request):
    return render(request, 'register.html')

def counter(request):
    words = request.POST['text']
    numWords = len(words.split())
    return render(request, 'countWords.html', { 'numWords' : numWords})


