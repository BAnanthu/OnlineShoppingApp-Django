# Generated by Django 3.0.6 on 2020-05-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineShoppingApp', '0005_auto_20200522_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_shortinfo',
            field=models.TextField(default='nil'),
        ),
    ]