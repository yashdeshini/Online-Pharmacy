from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),  # Ensure this line is present
]
