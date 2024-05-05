from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Access the cleaned form data
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if passwords match
            if password != confirm_password:
                # Handle password mismatch error
                # For simplicity, let's just return to the signup page with an error message
                return render(request, 'signup/signup.html', {'form': form, 'error_message': 'Passwords do not match'})

            # Create the user
            user = User.objects.create_user(username=email, email=email, password=password, first_name=fullname)
            user.save()

            # Automatically log in the user after signup
            user = authenticate(username=email, password=password)
            login(request, user)

            # Redirect to the login page after successful signup
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})
