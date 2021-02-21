# Generated by Django 3.1.5 on 2021-02-03 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0022_auto_20210202_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='brand',
        ),
        migrations.AddField(
            model_name='stock',
            name='batch_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_batch_item', to='stock_system.batchitems'),
        ),
    ]
