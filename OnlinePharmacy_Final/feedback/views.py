from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
#from . models import Product, Cart, CartItem, Feedback, PasswordReset
from . import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Cart, CartItem, Product
import json, requests

def feedback_done(request):
    return HttpResponse("<h1> Feedback Done </h1>")


def feedback(request):
    print(request.method)
    if request.method == 'POST':
        print("2")
        product_data = {
            "Name": str(request.POST.get('name')),
            "Email": str(request.POST.get('email')),
            "Message": str(request.POST.get('message'))
        }

        json_data = json.dumps(product_data)
        payload = json.loads(json_data)
        print(json_data)

        response = requests.post("http://127.0.0.1:8000/feedback/", json=payload)
        
        if response.status_code == 200:
            return render(request, 'feedback.html')
        else:
            error_message = response.content.decode('utf-8')
            print("Error:", error_message)
            return HttpResponse("<h1>Error: {}</h1>".format(error_message))
        
    return render(request, 'feedback.html')


def feedback_thanks(request):
    return render(request, 'feedback_thanks.html')

# Create view for submitting feedback
'''class FeedbackCreateView(CreateView):
    model = models.Feedback
    fields = ['message', 'rating']
    template_name = 'feedback.html'
    success_url = '/feedback-thanks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# View for creating a password reset request
class PasswordResetCreateView(CreateView):
    model = models.PasswordReset
    fields = ['email']
    template_name = 'password.html'
    success_url = '/reset-instructions/'

    def form_valid(self, form):
        return super().form_valid(form)


# Simple home page view
class HomeView(View):
    def get(self, request):
        return render(request, 'feedback/home.html')


# View for listing products
class ProductListView(ListView):
    model = models.Product
    template_name = 'feedback/product_list.html'
    context_object_name = 'products'

#@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart.items.all()})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')


@login_required
def update_cart_item(request, item_id):
    quantity = request.POST.get('quantity', 0)
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.quantity = int(quantity)
    cart_item.save()
    return redirect('view_cart')

# Reset instructions page for password reset
def reset_instructions(request):
    return render(request, 'feedback/reset_instructions.html')
'''
