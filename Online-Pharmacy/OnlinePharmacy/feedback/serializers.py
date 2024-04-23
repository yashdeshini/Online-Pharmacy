from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Product, Cart, CartItem, Feedback

UserModel = get_user_model()

# Serializer for the Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']


# Serializer for the CartItem model
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']


# Serializer for the Feedback model
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['user', 'message', 'rating']


# Serializer for User password reset
class UserPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        # Check if user exists
        if not UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def create(self, validated_data):
        # Create or update the cart item
        cart, _ = Cart.objects.get_or_create(user=self.context['request'].user)
        cart_item, _ = CartItem.objects.update_or_create(
            cart=cart,
            product=validated_data['product'],
            defaults={'quantity': validated_data['quantity']}
        )
        return cart_item