from django.db import models
from django.conf import settings
from Products.models import Product

# Create your models here.




class AddToCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    print("user :" + settings.AUTH_USER_MODEL)
    product = models.ForeignKey(Product, default="nil", on_delete=models.SET_DEFAULT)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "CART"

    def __str__(self):
        return self.product.product_name
