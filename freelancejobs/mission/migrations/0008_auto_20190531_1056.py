# Generated by Django 2.2 on 2019-05-31 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0007_auto_20190531_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='localtion',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='mission',
            name='createdBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
