from django.urls import path
from . import views

urlpatterns = [
    path('', views.delete_products, name='delete_products'),
    path('product-deleted/', views.product_delete_successfully, name='success_url')
]
