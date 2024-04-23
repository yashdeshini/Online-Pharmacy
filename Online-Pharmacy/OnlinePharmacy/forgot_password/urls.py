from django.urls import path
from . import views

urlpatterns = [
    path('', views.forgot_password, name='forgot_password'),
]
