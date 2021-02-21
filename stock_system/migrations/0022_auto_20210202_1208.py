# Generated by Django 3.1.5 on 2021-02-02 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0021_brand_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='stock',
        ),
        migrations.AddField(
            model_name='brand',
            name='batch_item',
            field=models.ManyToManyField(blank=True, related_name='brand_batches', to='stock_system.BatchItems'),
        ),
    ]