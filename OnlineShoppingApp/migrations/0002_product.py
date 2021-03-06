# Generated by Django 3.0.6 on 2020-05-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineShoppingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.FileField(upload_to='documents')),
                ('product_brand', models.CharField(max_length=50)),
                ('product_highlights', models.CharField(max_length=100)),
                ('product_specification', models.CharField(max_length=100)),
                ('product_instock', models.IntegerField()),
                ('product_category', models.CharField(max_length=50)),
                ('product_price', models.IntegerField()),
                ('product_star_rating', models.IntegerField()),
                ('product_number_of_ratings', models.IntegerField()),
                ('product_offeroff', models.IntegerField()),
                ('product_discount', models.IntegerField()),
                ('product_dealprice', models.IntegerField()),
            ],
        ),
    ]
