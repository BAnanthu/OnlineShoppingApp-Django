from django.urls import path
from . import views

urlpatterns = [
    path('PaymentMethods/<int:product_id>/', views.PaymentMethods)

]
