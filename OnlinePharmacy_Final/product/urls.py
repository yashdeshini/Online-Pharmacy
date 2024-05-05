from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home,name='home'),
    path('heart.html', views.heart, name='heart'),
    path('diabetes.html', views.diabetes, name='diabetes'),
    path('vitamins.html', views.vitamins, name='vitamins'),
    path('supplements.html', views.supplements, name='supplements'),
    path('flu.html', views.flu, name='flu'),
    path('dental.html', views.dental, name='dental'),
    path('feedback/', include('feedback.urls')),
    path('homo.html', views.homo, name='homo'),
    path('otc.html', views.otc, name='otc'),
]