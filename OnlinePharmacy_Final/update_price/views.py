from django.shortcuts import render
from django.http import HttpResponse
import requests, json

def update_price(request):
    if request.method == 'POST':
        product_data = {
            "ProductImage": str(request.POST.get('confirmation')),
            "ProductName": str(request.POST.get('productName')),
            "ProductPrice": str(request.POST.get('productPrice')),
            "ProductDescription": str(request.POST.get('productDescription')),
            "ProductRatings": str(request.POST.get('productRatings')),
            "Category": str(request.POST.get('productCategory'))
        }

        json_data = json.dumps(product_data)
        payload = json.loads(json_data)
        print(json_data)

        response = requests.post("http://127.0.0.1:8000/products/update", json=payload)
        
        if response.status_code == 200:
            return HttpResponse("<h1>Success</h1>")
        else:
            error_message = response.content.decode('utf-8')
            print("Error:", error_message)
            return HttpResponse("<h1>Error: {}</h1>".format(error_message))

    return render(request, 'update_price.html')


def product_updated_successfully(request):
    return render(request, 'product_updated_successfully.html')