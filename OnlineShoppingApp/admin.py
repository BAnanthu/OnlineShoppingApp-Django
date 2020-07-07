from django.contrib import admin
from Products.models import Product
from Products.models import TodaysDeals,NewItems
from .models import AddToCart

# Register your models here.
# # admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(TodaysDeals)
# admin.site.register(NewItems)
admin.site.register(AddToCart)