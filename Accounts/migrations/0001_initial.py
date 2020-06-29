# Generated by Django 3.0.6 on 2020-06-28 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_DOB', models.DateField(default='2020-01-01')),
                ('customer_gender', models.CharField(default='nil', max_length=10)),
                ('customer_address', models.TextField(default='nil')),
                ('customer_contact', models.CharField(default='nil', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]