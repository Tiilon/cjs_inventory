# Generated by Django 3.1.5 on 2021-02-01 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_system', '0019_auto_20210201_2244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batchid',
            options={'ordering': ('-created_at',)},
        ),
    ]