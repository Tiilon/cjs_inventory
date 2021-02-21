# Generated by Django 3.1.5 on 2021-02-03 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_system', '0023_auto_20210203_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('date_dispatched', models.DateTimeField(default=django.utils.timezone.now)),
                ('dispatched_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispatches', to=settings.AUTH_USER_MODEL)),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock', to='stock_system.stock')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='dispatches',
            field=models.ManyToManyField(blank=True, related_name='stock_dispatches', to='stock_system.Dispatched'),
        ),
    ]