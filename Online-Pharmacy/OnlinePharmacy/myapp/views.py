from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

def defaultView(request):
    return HttpResponse("<h1>Default View</h1>")


def getProduct(request):
    response = requests.get("http://127.0.0.1:8000/products/sprin")
    return JsonResponse(response.json(), safe=False)


def getUser(request):
    response = requests.get("http://127.0.0.1:8000/users/kaneri")
    return JsonResponse(response.json(), safe=False)


def getPharma(request):
    response = requests.get("http://127.0.0.1:8000/pharamacist/micheal")
    return JsonResponse(response.json(), safe=False)

def paymentGateway(request):
    
    data = {
        "CardType": "VISA",
        "Owner": "XXXXX Wade",
        "CardNumber": "XXXX401241555524",
        "CardExpiry": "XX-XX",
        "CVV": "XXX"
    }
    
    # Send a GET request with the dictionary as query parameters
    response = requests.get("http://127.0.0.1:8000/paymentCheck/", params = data)
    return JsonResponse(response.json(), safe=False)

