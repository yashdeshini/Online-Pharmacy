from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def vita(request):
    return render(request, 'vita.html')

def persc(request):
    return render(request, 'persc.html')

def health(request):
    return render(request, 'health.html')

def baby(request):
    return render(request, 'baby.html')

def dear(request):
    return render(request, 'dear.html')

def wt(request):
    return render(request, 'wt.html')

def homo(request):
    return render(request, 'homo.html')

def otc(request):
    return render(request, 'otc.html')