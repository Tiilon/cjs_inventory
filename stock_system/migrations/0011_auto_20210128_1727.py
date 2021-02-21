# Generated by Django 3.1.5 on 2021-01-28 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0010_auto_20210128_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batchitems',
            name='brand',
        ),
        migrations.AddField(
            model_name='batchitems',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='batch_brand', to='stock_system.brand'),
        ),
    ]