from django.shortcuts import render, redirect
import requests, json
from django.http import HttpResponse

def add_products(request):

    if request.method == 'POST':
        product_data = {
            "ProductImage": str(request.POST.get('productName')),
            "ProductName": str(request.POST.get('productName')),
            "ProductPrice": str(request.POST.get('productPrice')),
            "ProductDescription": str(request.POST.get('productManufacturer')),
            "ProductRatings": str(request.POST.get('productDescription')),
            "Category": str(request.POST.get('productComposition'))
        }

        json_data = json.dumps(product_data)
        payload = json.loads(json_data)
        print(json_data)

        response = requests.post("http://127.0.0.1:8000/products/add", json=payload)
        
        if response.status_code == 200:
            return HttpResponse("<h1>Success</h1>")
        else:
            error_message = response.content.decode('utf-8')
            print("Error:", error_message)
            return HttpResponse("<h1>Error: {}</h1>".format(error_message))
    
    return render(request, 'add_products.html')


def product_added_successfully(request):
    return render(request, 'product_added_successfully.html')