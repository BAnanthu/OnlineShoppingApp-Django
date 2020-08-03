from django.urls import path
from . import views

urlpatterns = [
    path('productdetails/<int:product_id>/', views.productDetails),
]
