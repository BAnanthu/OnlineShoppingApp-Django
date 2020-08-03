from django.urls import path
from . import views

urlpatterns = [
    path('Order/<int:product_id>/', views.Order),
    path('removeOrderItem/<int:order_id>/', views.removeOrderItem),
    path('myOrders/', views.myOrders)
]
