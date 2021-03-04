from random import randrange
from django.conf import settings
from django.db import models
from django.utils import timezone


# class Client(models.Model):
#     name_of_owner = models.CharField(blank=True,null=True, max_length=250)
#     name_of_company = models.CharField(max_length=250, blank=True, null=True)
#     contact = models.CharField(max_length=20, blank=True, null=True)

PACKAGE = {
    ('Box', 'Box'),
    ('Carton', 'Carton')
}


class Brand(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    item = models.CharField(max_length=250, null=True, blank=True)
    no_available = models.IntegerField(default=0, null=True, blank=True)
    no_units_dispatched = models.IntegerField(default=0, null=True, blank=True)
    reorder_lvl = models.IntegerField(default=0, null=True, blank=True)
    no_units_left = models.IntegerField(default=0, null=True, blank=True)
    dispatches = models.ManyToManyField('Dispatched', related_name='brand_dispatches', blank=True)
    batch_item = models.ManyToManyField('BatchItems', related_name='brand_batches', blank=True)
    # client = models.ManyToManyField(Client, related_name='clients_brands', blank=True)

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
    batch_item = models.ManyToManyField('BatchItems', related_name='batch_items', blank=True)
    complete = models.BooleanField(default=False)
    request_del = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='batch_id', on_delete=models.SET_NULL, blank=True, null=True)
    # client = models.ForeignKey(Client, related_name='client_batches', on_delete=models.SET_NULL, blank=True, null=True)

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
    created_at = models.DateTimeField(default=timezone.now)
    received_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='batches',blank=True, null=True)

    def __str__(self):
        return f"{self.brand} | {self.boxes_received}"


class Stock(models.Model):
    brand = models.ForeignKey('Brand', related_name='stock_brand', on_delete=models.SET_NULL,blank=True, null=True)
    dispatches = models.ManyToManyField('Dispatched', related_name='stock_dispatches', blank=True)
    no_units_available = models.IntegerField(default=0, null=True, blank=True)
    no_units_dispatched = models.IntegerField(default=0, null=True, blank=True)
    no_units_left = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.no_units_available}"


class Dispatched(models.Model):
    number = models.IntegerField(default=0, null=True, blank=True)
    date_dispatched = models.DateTimeField(default=timezone.now)
    dispatched_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='dispatches', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='brand_dispatches', blank=True, null=True)

    def __str__(self):
        return f"{self.number}"

    class Meta:
        ordering = ('-date_dispatched',)


REASONS = {
    ('Expired', 'Expired'),
    ('Damaged', 'Damaged'),
    ('Unwanted', 'Unwanted')
}


class Returns(models.Model):
    brand = models.ForeignKey(Brand, related_name='brand_returns', on_delete=models.SET_NULL, blank=True, null=True)
    number = models.IntegerField(default=0, blank=True, null=True)
    reason = models.CharField(max_length=250, blank=True, null=True, choices=REASONS)
    date_returned = models.DateTimeField(default=timezone.now, null=True, blank=True)
    received_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='returns', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.number}"

    class Meta:
        ordering = ('-date_returned',)