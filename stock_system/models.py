from random import randrange
from django.conf import settings
from django.db import models
from django.utils import timezone


# class Client(models.Model):
#     name_of_owner = models.CharField(blank=True,null=True, max_length=250)
#     name_of_company = models.CharField(max_length=250, blank=True, null=True)


class Brand(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    item = models.CharField(max_length=250, null=True, blank=True)
    batch_item = models.ManyToManyField('BatchItems', related_name='brand_batches', blank=True)
    # client = models.ForeignKey(Client, related_name='clients_brand', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.item}"


def generate():
    FROM = '0123456789'
    LENGTH = 5
    batch_no = ""
    for i in range(LENGTH):
        batch_no += FROM[randrange(0, len(FROM))]

    return f"Batch#{batch_no}"


class BatchId(models.Model):
    batch_id = models.CharField(default=generate, max_length=100, editable=False, unique=True)
    # brand = models.ManyToManyField('Brand', related_name='brands', blank=True)
    batch_item = models.ManyToManyField('BatchItems', related_name='batch_items', blank=True)
    complete = models.BooleanField(default=False)
    request_del = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='batch_id', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.batch_id}"

    class Meta:
        ordering = ('-created_at',)


class BatchItems(models.Model):
    batch = models.ForeignKey(BatchId, related_name='batch_items', null=True, on_delete=models.SET_NULL,blank=True)
    brand = models.ForeignKey('Brand', related_name='batch_brand', blank=True, null=True, on_delete=models.SET_NULL)
    boxes_received = models.IntegerField(default=0, null=True, blank=True)
    units_per_box = models.IntegerField(default=0, null=True, blank=True)
    total_units = models.IntegerField(default=0, null=True, blank=True)
    man_date = models.DateTimeField(null=True, blank=True)
    exp_date = models.DateTimeField(blank=True, null=True)
    received_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='batches',blank=True, null=True)

    def __str__(self):
        return f"{self.brand} | {self.boxes_received}"


class Stock(models.Model):
    batch_item = models.ForeignKey('BatchItems', related_name='stock_batch_item', on_delete=models.SET_NULL,blank=True, null=True)
    dispatches = models.ManyToManyField('Dispatched', related_name='stock_dispatches', blank=True)
    no_units_available = models.IntegerField(default=0, null=True, blank=True)
    no_units_dispatched = models.IntegerField(default=0, null=True, blank=True)
    no_units_left = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.batch_item.brand}"


class Dispatched(models.Model):
    number = models.IntegerField(default=0, null=True, blank=True)
    date_dispatched = models.DateTimeField(default=timezone.now)
    dispatched_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='dispatches', blank=True, null=True)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, related_name='stock', blank=True, null=True)

    def __str__(self):
        return f"{self.stock.batch_item.brand} || {self.number}"

    class Meta:
        ordering = ('-date_dispatched',)


class Returns(models.Model):
    brand = models.ForeignKey(Brand, related_name='brand_returns', on_delete=models.SET_NULL, blank=True, null=True)
    number = models.IntegerField(default=0, blank=True, null=True)
    reason = models.CharField(max_length=250, blank=True, null=True)
    date_returned = models.DateTimeField(default=timezone.now, null=True, blank=True)
    received_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='returns', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.brand}"

    class Meta:
        ordering = ('-date_returned',)