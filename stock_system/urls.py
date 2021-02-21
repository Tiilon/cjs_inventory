from django.urls import path
from .views import *


app_name = 'stock_system'

urlpatterns = [
    path('add_staff/', AddStaff.as_view(), name='new-staff'),
    path('management/', management_view, name='management_page'),
    path('stock/', stock, name='stock_page'),
    path('raise/batch_id/', add_batch, name='new_batch'),
    path('batch_id/list/', batch_id_list, name='batch_list'),
    path('batch/details/<id>/', batch_details, name='batch-details'),
    path('stock/dispatch/<id>/', stock_dispatch, name='dispatch_stock'),
    path('items/returns/', returns, name='returned_items'),
    path('batch/complete/<id>/', complete_batch, name='complete_batch'),
    path('batch/request/del/<id>/', request_del_batch, name='request_del_batch'),
    path('batch/approve/del/<id>/', approve_del, name='approve_del_batch'),
    path('batch/request/list/', delete_request_list, name='delete_request_list')
]