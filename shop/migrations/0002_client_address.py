# Generated by Django 3.2.15 on 2022-11-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]