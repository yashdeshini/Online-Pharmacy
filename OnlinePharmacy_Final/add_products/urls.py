from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_products, name='add_products'),  # Ensure this line is present
    path('product-added/', views.product_added_successfully, name='success_url')
]
