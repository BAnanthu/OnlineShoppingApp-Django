from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_DOB = models.DateField(default='2020-01-01')
    customer_gender = models.CharField(max_length=10, default='nil')
    customer_address = models.TextField(default='nil')
    customer_contact = models.CharField(max_length=10, default='nil')

    def __str__(self):
        # print("self.user.username ==")
        # print(self.user.username)
        return self.user.username

