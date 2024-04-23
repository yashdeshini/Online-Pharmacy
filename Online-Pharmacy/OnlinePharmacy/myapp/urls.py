from django.urls import path
from . import views

urlpatterns = [
    path('', views.defaultView),
    path('getProduct/', views.getProduct),
    path('getUser/', views.getUser),
    path('getPharma/', views.getPharma),
    path('payment/', views.paymentGateway),
]