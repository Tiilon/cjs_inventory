import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, TemplateView
from stock_system.forms import UserForm, BrandForm, BatchItemsForm, DispatchForm, ReturnForm
from stock_system.models import Stock, Brand, BatchId, generate, BatchItems, Returns, Dispatched
from users.models import User


def apps_view(request):
    return render(request, 'layout/apps.html')


class AddStaff(LoginRequiredMixin, CreateView):
    template_name = 'management/staff_new.html'
    form_class = UserForm
    success_url = reverse_lazy('stock_system:dashboard')
    queryset = User.objects.all()

    def form_valid(self, form):
        valid = super(AddStaff, self).form_valid(form)
        form.instance.set_password(form.instance.password)
        form.save()
        return valid


def management_view(request):
    brand_form = BrandForm
    batch = BatchId.objects.all()
    batch_to_del = BatchId.objects.filter(request_del = True)
    day1 = timezone.now()
    days_to_show = datetime.timedelta(days=1)
    day_returns = day1 + days_to_show
    returns = Returns.objects.filter(date_returned__lte=day_returns)
    dispatch = Dispatched.objects.filter(date_dispatched__lte=day_returns)
    
    context = {
        'brand_form': brand_form,
        'returns':returns,
        'dispatches':dispatch,
        'batch':batch,
        'batch_to_del':batch_to_del
    }

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('stock_system:management_page'))
    return render(request, 'management/management_dashboard.html', context)


def stock(request):
    stock = Stock.objects.all()
    form = DispatchForm
    context = {
        'stock': stock,
        'form': form
    }
    return render(request=request, template_name='stock/stock_sheet.html', context=context)


def stock_dispatch(request, id):
    stock = Stock.objects.get(id=id)
    brand =Brand.objects.all()
    form = DispatchForm
    form2 = ReturnForm

    context = {
        'brand': brand,
        'stock': stock,
        'returns':returns,
        'form': form,
        'form2':form2
    }

    if request.method == 'POST':
        form = DispatchForm(request.POST)
        if form.is_valid():
            form.instance.dispatched_by = request.user
            form.instance.stock = stock
            form.save()
        stock.dispatches.add(form.instance)
        stock.no_units_dispatched += form.instance.number
        stock.no_units_left = stock.no_units_available - stock.no_units_dispatched
        stock.save()
        return redirect(reverse_lazy('stock_system:stock_page'))
    return render(request, 'stock/stock_details.html', context)


def batch_id_list(request):
    batch_id = BatchId.objects.all()
    context = {
        'batch_id': batch_id
    }
    return render(request, 'stock/batch_list.html', context)


def add_batch(request):
    BatchId.objects.all()

    if request.method == 'POST':
        new_batch = BatchId.objects.create(
            batch_id=generate(),
            created_by=request.user,
            created_at=timezone.now(),
        )
        new_batch.save()
    return redirect(reverse_lazy('stock_system:batch_list'))


def batch_details(request, id):
    batch = BatchId.objects.get(id=id)
    batch_item = BatchItems.objects.all()
    brands = Brand.objects.all()
    boxes_received = request.POST.get('boxes_received')
    units_per_box = request.POST.get('units_per_box')
    man_date = request.POST.get('man_date')
    exp_date = request.POST.get('exp_date')
    form = BatchItemsForm
    context = {
        'batch': batch,
        'form': form,
        'brand': brands,
        'batch_item': batch_item,
        'error': ''
    }
    if request.method == "POST":
        total_units = int(boxes_received) * int(units_per_box)
        brand = Brand.objects.get(id=request.POST.get('brand'))
        exp_date = datetime.datetime.strptime(exp_date, '%Y-%m-%d').date()
        current_date = timezone.now().date()
        if exp_date <= current_date:
            error = "This product is expired"
            context['error'] = error
            return render(request, 'stock/batch_details_batch.html', context)
        try:
            BatchItems.objects.get(brand=brand, batch=batch)
            error = "There's already an item with this brand recorded"
            context['error'] = error
            return render(request, 'stock/batch_details_batch.html', context)
        except BatchItems.DoesNotExist:
            new_batch_items = BatchItems.objects.create(
                batch=batch,
                brand=brand,
                boxes_received=boxes_received,
                units_per_box=units_per_box,
                total_units=total_units,
                man_date=man_date,
                exp_date=exp_date,
                received_by=request.user
            )
            try:
                stock = Stock.objects.get(batch_item__brand=brand)
                stock.no_units_available += new_batch_items.total_units
                stock.save()
            except Stock.DoesNotExist:
                new_stock = Stock.objects.create(
                    batch_item=new_batch_items,
                    no_units_available=total_units
                )

            batch.batch_item.add(new_batch_items)
            brand.batch_item.add(new_batch_items)
            brand.save()
            batch.save()

        return redirect(reverse_lazy('stock_system:batch-details', kwargs={'id': id}))
    return render(request, 'stock/batch_details_batch.html', context)


def make_returns(request, id):
    stock = Stock.objects.get(id=id)
    form = ReturnForm

    context = {
        'stock': stock,
        'form': form
    }

    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.instance.stock = stock
            if form.instance.reason == 'Unwanted':
                stock.no_units_left += form.instance.number
            form.instance.date_returned = timezone.now()
            form.instance.received_by = request.user
            form.save()
            stock.save()
    return redirect(reverse_lazy('stock_system:returned_items'))


def returns(request):
    brand = Brand.objects.all()
    returns = Returns.objects.all()

    context = {
        'brand': brand,
        'returns': returns
    }

    # if request.method == 'POST':
    #     new_return = Returns.objects.create(
    #         brand=Brand.objects.get(id=request.POST.get('brand')),
    #         number=request.POST.get('number'),
    #         reason=request.POST.get('reason'),
    #         received_by= request.user
    #     )
    return render(request, 'stock/returns.html', context=context)


def complete_batch(request, id):
    batch=BatchId.objects.get(id=id)

    if request.method == 'POST':
        batch.complete = True
        batch.save()
    return redirect('stock_system:stock_page')


def request_del_batch(request, id):
    batch = BatchId.objects.get(id=id)

    if request.method == 'POST':
        batch.request_del = True
        batch.save()
    return redirect('stock_system:stock_page')


def delete_request_list(request):
    batch = BatchId.objects.filter(request_del=True)

    context = {
        'batch':batch
    }
    return render(request, 'stock/del_req_list.html', context)


def approve_del(request, id):
    batch = BatchId.objects.get(id=id)
    items = BatchItems.objects.filter(id=batch.id)

    if request.method == 'POST':
        items.delete()
        batch.delete()
    return redirect(reverse_lazy('stock_system:delete_request_list'))


