# Generated by Django 2.2 on 2019-05-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='İrtibat Numarası'),
        ),
    ]
