from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_summary, name='cart'),
    path('add/', views.cart_add, name='cart_add'),
    path('delete/<int:product_id>/', views.cart_delete, name='cart_delete'),
    path('update', views.cart_update, name='cart_update'),
]
