from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from cryptography.fernet import Fernet
from django.http import HttpResponse
import json, requests

key = b'8SPmp50NR8qvXUf4XAtDQFViHTJQafe5xhmH9Vqm7DY='

def signup(request):
    if request.method == 'POST':
        print(str(request.POST.get('username')))
        fullname = str(request.POST.get('username'))
        email = str(request.POST.get('email'))
        password = str(request.POST.get('password'))
        confirm_password = str(request.POST.get('confirm_password'))
        name_parts = fullname.split()
        firstname = name_parts[0]
        lastname = name_parts[-1] if len(name_parts) > 1 else ""

        if password == confirm_password:
            fernet = Fernet(key)
            encPassword = fernet.encrypt(password.encode())
            
            person_data = {
                "Email": email,
                "Password": str(encPassword),
                "ContactNumber": "",
                "FName": firstname,
                "LName": lastname,
                "DateofBirth": "",
                "Gender": "",
                "Orders": [],
                "City": "",
                "Street": "",
                "State": "",
                "Pincode": ""
            }
            
            json_data = json.dumps(person_data)
            payload = json.loads(json_data)

            response = requests.post("http://127.0.0.1:8000/users/add", json=payload)
            
            if response.status_code == 200:
                return redirect('/accounts/login/')
            else:
                error_message = response.content.decode('utf-8')
                print("Error:", error_message)
                return HttpResponse("<h1>Error: {}</h1>".format(error_message))
            
        return redirect('/signup/')

    return render(request, 'signup.html')

def user_added_successfully(request):
    return render(request, 'user_added_successfully.html')