# Generated by Django 3.1.7 on 2021-02-23 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0035_auto_20210223_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returns',
            name='stock',
        ),
        migrations.AddField(
            model_name='returns',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_returns', to='stock_system.brand'),
        ),
        migrations.AlterField(
            model_name='returns',
            name='reason',
            field=models.CharField(blank=True, choices=[('Expired', 'Expired'), ('Damaged', 'Damaged'), ('Unwanted', 'Unwanted')], max_length=250, null=True),
        ),
    ]