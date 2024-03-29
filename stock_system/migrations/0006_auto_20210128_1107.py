# Generated by Django 3.1.5 on 2021-01-28 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stock_system.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_system', '0005_auto_20210118_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.CharField(default=stock_system.models.generate, editable=False, max_length=100, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='batch_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BatchItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boxes_received', models.IntegerField(blank=True, null=True)),
                ('units_per_box', models.IntegerField(blank=True, null=True)),
                ('total_units', models.IntegerField(blank=True, null=True)),
                ('man_date', models.DateTimeField(blank=True, null=True)),
                ('exp_date', models.DateTimeField(blank=True, null=True)),
                ('batch_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='batch_items', to='stock_system.batchid')),
                ('received_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='batches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='no_units',
            new_name='no_units_available',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='batch',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.AddField(
            model_name='batchitems',
            name='stock',
            field=models.ManyToManyField(blank=True, related_name='stocks', to='stock_system.Stock'),
        ),
    ]
