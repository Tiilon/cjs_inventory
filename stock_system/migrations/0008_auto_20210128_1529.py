# Generated by Django 3.1.5 on 2021-01-28 15:29

from django.db import migrations, models
import stock_system.models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0007_auto_20210128_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchid',
            name='batch_id',
            field=models.CharField(default=stock_system.models.generate, editable=False, max_length=100, unique=True),
        ),
    ]
