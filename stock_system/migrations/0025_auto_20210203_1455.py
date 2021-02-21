# Generated by Django 3.1.5 on 2021-02-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0024_auto_20210203_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchitems',
            name='boxes_received',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='batchitems',
            name='total_units',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='batchitems',
            name='units_per_box',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='dispatched',
            name='number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='no_units_available',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='no_units_dispatched',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='no_units_left',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]