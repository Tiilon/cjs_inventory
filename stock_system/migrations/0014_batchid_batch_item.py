# Generated by Django 3.1.5 on 2021-01-29 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0013_auto_20210129_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchid',
            name='batch_item',
            field=models.ManyToManyField(blank=True, related_name='batch_items', to='stock_system.BatchItems'),
        ),
    ]