from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'basic.html')

def counter(request):
    #getting the text from the text area
    words = request.GET['text']
    #counting words and assiging values
    numWords = len(words.split())
    #connecting new file and variables
    return render(request, 'countWords.html', { 'numWords' : numWords})


