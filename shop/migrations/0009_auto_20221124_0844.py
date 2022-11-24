# Generated by Django 3.2.15 on 2022-11-24 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20221124_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=100, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Имя'),
        ),
    ]