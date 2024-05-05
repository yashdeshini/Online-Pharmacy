from django.shortcuts import render
from django.http import HttpResponse
import requests, json

def delete_products(request):
    if request.method == 'POST':
        product_data = {
            "ProductImage": str(request.POST.get('confirmation')),
            "ProductName": str(request.POST.get('product_id')),
            "ProductPrice": "",
            "ProductDescription": "",
            "ProductRatings": "",
            "Category": ""
        }

        json_data = json.dumps(product_data)
        payload = json.loads(json_data)
        print(json_data)

        response = requests.post("http://127.0.0.1:8000/products/remove", json=payload)
        
        if response.status_code == 200:
            return HttpResponse("<h1>Success</h1>")
        else:
            error_message = response.content.decode('utf-8')
            print("Error:", error_message)
            return HttpResponse("<h1>Error: {}</h1>".format(error_message))

    return render(request, 'delete_products.html')


def product_delete_successfully(request):
    return render(request, 'product_delete_successfully.html')