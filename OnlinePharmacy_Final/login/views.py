# login/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
from cryptography.fernet import Fernet, InvalidToken

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        response = requests.get('http://127.0.0.1:8000/users/{}/'.format(email))
        
        if response.status_code == 200:
            content = response.json()
            passwrd = content[0]['Password'].encode()
            
            key = b'8SPmp50NR8qvXUf4XAtDQFViHTJQafe5xhmH9Vqm7DY='
            fernet = Fernet(key)
            decMessage = fernet.decrypt(passwrd).decode()
            
            if password == decMessage:
                return redirect('home')
        else:
            error_message = response.content.decode('utf-8')
            print("Error:", error_message)
            return HttpResponse("<h1>Error: {}</h1>".format(error_message))

    return render(request, 'login.html')
    '''user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            # Return an invalid login message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html') '''

@login_required
def profile_view(request):
    return render(request, 'profile.html')