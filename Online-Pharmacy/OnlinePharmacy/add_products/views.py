from django.shortcuts import render

def add_products(request):
    return render(request, 'add_products.html')
