# Generated by Django 3.1.5 on 2021-02-01 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0017_auto_20210130_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='brand',
        ),
        migrations.AddField(
            model_name='stock',
            name='brand',
            field=models.ManyToManyField(blank=True, related_name='stock_brands', to='stock_system.Brand'),
        ),
    ]