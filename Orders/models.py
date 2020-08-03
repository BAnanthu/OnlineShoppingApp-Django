from django.db import models
from django.conf import settings
from Products.models import Product

# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING,null=True)
    order_id = models.AutoField(primary_key=True)
    order_customer_id = models.IntegerField(null=True)
    order_date = models.DateField(null=True)
    order_quantity = models.IntegerField(null=True, default=1)
    order_delivery_date = models.DateField(null=True)
    order_shipping_charge = models.IntegerField(null=True)
    order_deal_price = models.IntegerField(null=True)
    order_payment_method = models.CharField(max_length=50,null=True)
    order_status = models.CharField(max_length=50,default="success")
    class Meta:
        verbose_name_plural = "ORDER DETAILS"

    def __str__(self):
        return self.product.product_name