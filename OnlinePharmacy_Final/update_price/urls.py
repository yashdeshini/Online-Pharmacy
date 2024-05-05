from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_price, name='update_price'),
    path('product-updated/', views.product_updated_successfully, name='success_url')
]
