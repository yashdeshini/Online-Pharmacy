from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    #path('user-added/', views.user_added_successfully, name='success_url')
]
