# Generated by Django 3.1.5 on 2021-01-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0009_remove_stock_item_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batchitems',
            name='stock',
        ),
        migrations.AddField(
            model_name='batchitems',
            name='brand',
            field=models.ManyToManyField(blank=True, related_name='stocks', to='stock_system.Brand'),
        ),
    ]
