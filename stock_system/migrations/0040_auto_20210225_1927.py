# Generated by Django 3.1.7 on 2021-02-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0039_auto_20210225_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batchid',
            name='client',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='client',
        ),
        migrations.AlterField(
            model_name='returns',
            name='reason',
            field=models.CharField(blank=True, choices=[('Damaged', 'Damaged'), ('Expired', 'Expired'), ('Unwanted', 'Unwanted')], max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
