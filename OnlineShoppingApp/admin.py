from django.contrib import admin
from .models import Product
from .models import TodaysDeals,NewItems,AddToCart

# Register your models here.
# admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(TodaysDeals)
admin.site.register(NewItems)
admin.site.register(AddToCart)