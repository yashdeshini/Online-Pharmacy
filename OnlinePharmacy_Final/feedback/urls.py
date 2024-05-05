from django.urls import path
#from django.contrib import admin
from . import views
#from . import api_views
'''from . views import (
    ProductListView,
    DetailView,
    add_to_cart,
    remove_from_cart, 
    #FeedbackCreateView,
    PasswordResetCreateView,
    HomeView,
    feedback_thanks,
    reset_instructions
)'''

#app_name = 'feedback'

urlpatterns = [
    path('', views.feedback, name='feedback'),
    path('feedback_done/', views.feedback_done, name='feedback_done'),
    
    #path('feedback-thanks/', views.feedback_thanks, name='feedback_thanks'),
    #path('cart/', views.view_cart, name='view_cart'),
    #path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    #path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    #path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    #path('products/', ProductListView.as_view(), name='product_list'),
    #path('password/', PasswordResetCreateView.as_view(), name='password_reset'),
    #path('reset-instructions/', reset_instructions, name='reset_instructions'),
    #path('api/products/', api_views.ProductListAPI.as_view(), name='product-list'),
    #path('api/cart/add/', api_views.add_product_to_cart, name='add-to-cart'),
    #path('api/cart/remove/<int:pk>/', api_views.remove_product_from_cart, name='remove-from-cart'),
]