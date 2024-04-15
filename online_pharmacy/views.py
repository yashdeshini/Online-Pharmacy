from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    cart, _ = Cart.objects.get_or_create(id=request.session.get('cart_id'))
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    request.session['cart_id'] = cart.id
    return redirect('product_list')
