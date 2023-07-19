from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vasantha(request):
    return HttpResponse('<marquee><h1> MY NAME IS VASANTHA</h1></marquee')

def chaithanya(request):
    return HttpResponse('<marquee><i><h2>CHAITHU IS ONE OF MY FRIEND</h2></i></marquee>')