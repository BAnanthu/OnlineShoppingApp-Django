from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    # path('signup/', views.register),
    # path('signin/', views.login),
    # path('signout/', views.logout),
    path('productdetails/<int:product_id>/', views.productDetails),
    path('addingtocart/<int:product_id>/', views.addToCart),
    path('removeItem/<int:cart_id>/', views.removeItem),
    path('s/', views.search, name='search')
]
