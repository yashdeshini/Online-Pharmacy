from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('vita.html', views.vita, name='vita'),
    path('persc.html', views.persc, name='persc'),
    path('health.html', views.health, name='health'),
    path('baby.html', views.baby, name='baby'),
    path('dear.html', views.dear, name='dear'),
    path('wt.html', views.wt, name='wt'),
    path('homo.html', views.homo, name='homo'),
    path('otc.html', views.otc, name='otc'),
]