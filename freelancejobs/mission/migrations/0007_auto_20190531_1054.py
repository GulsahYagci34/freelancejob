# Generated by Django 2.2 on 2019-05-31 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0006_auto_20190531_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='mission',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mission.Category'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mission.Location'),
        ),
    ]
