from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_products, name='add_products'),  # Ensure this line is present
]
