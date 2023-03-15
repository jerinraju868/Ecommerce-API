# Generated by Django 4.1.3 on 2023-03-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_Home', '0004_checkout_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='paymentmethod',
            field=models.IntegerField(choices=[(1, 'Cash On Delivery'), (2, 'Google Pay'), (3, 'Paytm')]),
        ),
    ]
