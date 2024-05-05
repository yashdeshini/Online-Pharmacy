from rest_framework import generics, status, views
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Product, Cart, CartItem, Feedback,PasswordReset
from .serializers import (
    ProductSerializer,
    CartItemSerializer,
    FeedbackSerializer,
    UserPasswordResetSerializer
)
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

UserModel = get_user_model()

# API view for listing products
class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# API view for adding a product to cart
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product_to_cart(request, product_id):
    user = request.user
    try:
        product = Product.objects.get(id=product_id)
        cart, _ = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1  # Increase the quantity of the product if it's already in the cart
        cart_item.save()
        return Response({'status': 'product added'}, status=status.HTTP_201_CREATED)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


# API view for removing a product from cart
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_product_from_cart(request, product_id):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1  # Decrease the quantity
        else:
            cart_item.delete()  # Remove the item if quantity is 1
        return Response({'status': 'product removed'}, status=status.HTTP_204_NO_CONTENT)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
    except CartItem.DoesNotExist:
        return Response({'error': 'CartItem not found'}, status=status.HTTP_404_NOT_FOUND)


# API view for submitting feedback
class FeedbackCreateAPI(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# API view for user password reset request
@api_view(['POST'])
def password_reset_request(request):
    serializer = UserPasswordResetSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        associated_users = UserModel.objects.filter(email=email)
        if associated_users.exists():
            for user in associated_users:
                subject = "Password Reset Requested"
                email_template_name = "password/password_reset_email.txt"
                c = {
                    'email': user.email,
                    'domain': 'example.com',  # Or use your domain
                    'site_name': 'Website',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': PasswordResetTokenGenerator().make_token(user),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                except Exception as e:
                    return Response({'error': 'Email could not be sent'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': 'Password reset link has been sent if the email is registered'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
