from django.shortcuts import render
from django.http import HttpResponse
from .models import feature

# Create your views here.
def index(request):
    
    var1 = feature()
    var1.id = 0
    var1.name = "Font-color"
    var1.details = "Changes colors"
    
    var2 = feature()
    var2.id = 1
    var2.name = "Font-style"
    var2.details = "Changes Style"

    var3 = feature()
    var3.id = 2
    var3.name = "Font-Type"
    var3.details = "Changes type"

    vars = [var1, var2, var3]
    return render(request, 'basic.html', {'variables' : vars})

def counter(request):
    words = request.POST['text']
    numWords = len(words.split())
    return render(request, 'countWords.html', { 'numWords' : numWords})


