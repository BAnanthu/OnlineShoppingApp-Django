from django.contrib import admin
from .models import Product
from .models import TodaysDeals,NewItems,OfferZone
# Register your models here.
admin.site.register(Product)
admin.site.register(TodaysDeals)
admin.site.register(NewItems)
admin.site.register(OfferZone)