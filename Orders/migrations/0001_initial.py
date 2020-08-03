# Generated by Django 3.0.6 on 2020-07-12 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_customer_id', models.IntegerField()),
                ('order_date', models.DateField()),
                ('order_delivery_date', models.DateField()),
                ('order_shipping_charge', models.IntegerField()),
                ('order_deal_price', models.IntegerField()),
                ('order_payment_method', models.CharField(max_length=50)),
                ('order_status', models.CharField(default='success', max_length=50)),
                ('product', models.ForeignKey(default='nil', on_delete=django.db.models.deletion.DO_NOTHING, to='Products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ORDER DETAILS',
            },
        ),
    ]
