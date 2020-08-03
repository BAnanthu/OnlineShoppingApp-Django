from django.urls import path
from . import views

urlpatterns = [
    path('addingtocart/<int:product_id>/', views.addToCart),
    path('removeItem/<int:cart_id>/', views.removeItem),
    path('myCart/', views.myCart)
]
