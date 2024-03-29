# Generated by Django 4.1.3 on 2023-03-08 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Api_Home', '0008_rename_paymentmethod_checkout_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
