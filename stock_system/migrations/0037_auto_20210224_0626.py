# Generated by Django 3.1.7 on 2021-02-23 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0036_auto_20210223_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='reorder_lvl',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='returns',
            name='reason',
            field=models.CharField(blank=True, choices=[('Damaged', 'Damaged'), ('Expired', 'Expired'), ('Unwanted', 'Unwanted')], max_length=250, null=True),
        ),
    ]
