# Generated by Django 3.0.6 on 2020-06-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineShoppingApp', '0010_auto_20200601_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
