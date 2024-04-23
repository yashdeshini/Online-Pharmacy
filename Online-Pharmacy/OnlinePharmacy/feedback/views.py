from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
#from . models import Product, Cart, CartItem, Feedback, PasswordReset
from . import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Cart, CartItem, Product


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


# Create view for submitting feedback
class FeedbackCreateView(CreateView):
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


# Thanks page for feedback submission
def feedback_thanks(request):
    return render(request, 'feedback_thanks.html')


# Reset instructions page for password reset
def reset_instructions(request):
    return render(request, 'feedback/reset_instructions.html')