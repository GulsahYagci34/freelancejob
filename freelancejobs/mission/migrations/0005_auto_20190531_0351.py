# Generated by Django 2.2 on 2019-05-31 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0004_auto_20190531_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='startDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
    ]
