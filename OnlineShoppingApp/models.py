from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     customer_DOB = models.DateField(default='2020-01-01')
#     customer_gender = models.CharField(max_length=10, default='nil')
#     customer_address = models.TextField(default='nil')
#     customer_contact = models.CharField(max_length=10, default='nil')
#
#     def __str__(self):
#         # print("self.user.username ==")
#         # print(self.user.username)
#         return self.user.username


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

# class ProductReviews(models.Model):
#     product_id_fk =
#     ProductReviews_user_rating = models.IntigerField()
#     ProductReviews_user_comment = models.CharField(max_length=1000)
#     ProductReviews_user_image1 = models.FileField(upload_to="documents")
#     ProductReviews_user_image2 = models.FileField(upload_to="documents")
#     ProductReviews_user_image3 = models.FileField(upload_to="documents")
#     ProductReviews_user_image4 = models.FileField(upload_to="documents")
#     ProductReviews_likes =  models.IntigerField()
#     ProductReviews_dislikes =  models.IntigerField()

# class Orders(models.Model):
#     order_product_id = models.IntigerField()
#     order_customer_id =
#     order_date =
#     order_delivery_date =
#     order_shipping_charge =
#     order_deal_price =
#     order_payment_method =
#     order_status =
#
# class Return(models.model):
#     return_product_id =
#     return_customer_id =
#     return_sending_date =
#     return_receiving_date =
#     return_item_status =
#
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


class AddToCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    print("user :" + settings.AUTH_USER_MODEL)
    product = models.ForeignKey(Product, default="nil", on_delete=models.SET_DEFAULT)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "CART"

    def __str__(self):
        return self.product.product_name

# class BestSellers(models.Model):
#     bestSeller_brand =
#     bestSeller_product_id
