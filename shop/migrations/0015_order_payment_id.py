# Generated by Django 3.2.15 on 2022-11-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID оплаты Kassa 24'),
        ),
    ]