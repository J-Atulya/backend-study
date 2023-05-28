from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'basic.html')

def counter(request):
    words = request.POST['text']
    numOfWords = len(words.split())
    return render(request, 'countWords.html', {'Numofwords': numOfWords, 'sentence': words})
