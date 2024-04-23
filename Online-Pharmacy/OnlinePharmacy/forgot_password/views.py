from django.shortcuts import render

def forgot_password(request):
    return render(request, 'forgot_password.html')
