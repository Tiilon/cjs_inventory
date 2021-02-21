from django.forms import *
from users.models import *
from .models import *


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput(attrs={'required': True}), label = 'Password')

    class Meta:
        model = User
        fields = ('staff_id', 'first_name', 'last_name', 'user_type', 'password')

    def clean_staff_id(self):
        staff_id = self.cleaned_data.get('staff_id')

        try:
            User.objects.get(staff_id=staff_id)
            raise ValidationError('Staff with this staff id already exist')
        except User.DoesNotExist:
            pass

        return staff_id


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields=(
            'name',
            'item'
        )
        # widgets = {
        #     'name': TextInput(attrs={'class':'form-control'})


class BatchItemsForm(ModelForm):
    class Meta:
        model = BatchItems
        fields = (
            'brand',
            'boxes_received',
            'units_per_box',
            # 'total_units',
            'man_date',
            'exp_date',
        )
        widgets = {
            'man_date': DateInput(attrs={'type': 'date'}),
            'exp_date':DateInput(attrs={'type': 'date'}),
        }


class DispatchForm(ModelForm):
    class Meta:
        model= Dispatched
        fields = ('number',)
        widgets={
            'number': NumberInput(attrs={'placeholder': 'Enter quantity to dispatch....', 'required': True})
        }


class ReturnForm(ModelForm):
    class Meta:
        model = Returns
        fields = (
            'number',
            'reason',
            )
        widgets = {
            'number': NumberInput(attrs={'placeholder': 'Enter quantity returned....', 'required': True})
        }