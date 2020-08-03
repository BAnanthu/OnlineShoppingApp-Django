from django.db import models

# Create your models here.
class Product(models.Model):

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_image = models.FileField(upload_to="documents")
    product_brand = models.CharField(max_length=50)
    product_shortinfo = models.TextField(default='nil')
    product_highlights = models.TextField()
    product_specification = models.TextField()
    product_instock = models.IntegerField()
    product_category = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_star_rating = models.IntegerField()
    product_number_of_ratings = models.IntegerField()
    product_offeroff = models.IntegerField()
    product_discount = models.IntegerField()
    product_dealprice = models.IntegerField()

    class Meta:
        verbose_name_plural = "PRODUCT DETAILS"

    def __str__(self):
        return self.product_name

class TodaysDeals(models.Model):
    todaysDeal_product_fk = models.ForeignKey(Product,default="nil", on_delete=models.SET_DEFAULT)
    todaysDeal_offer_Off = models.IntegerField()
    todaysDeal_deal_price = models.IntegerField()

    class Meta:
        verbose_name_plural = "TODAY'S DEALS"

    def __str__(self):
        return self.todaysDeal_product_fk.product_name

class NewItems(models.Model):
    NewItems_product_fk = models.ForeignKey(Product,default="nil", on_delete=models.SET_DEFAULT)


    class Meta:
        verbose_name_plural = "NEW ITEMS"

    def __str__(self):
        return self.NewItems_product_fk.product_name


class OfferZone(models.Model):
    offerzone_product_fk = models.ForeignKey(Product,default="nil", on_delete=models.SET_DEFAULT)
    offerzone_Off = models.IntegerField()
    offerzone_deal_price = models.IntegerField()

    class Meta:
        verbose_name_plural = "OFFERS'S ZONE"

    def __str__(self):
        return self.offerzone_product_fk.product_name