from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone' ,'email', 'address']

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = 'Họ tên người nhận:'
        self.fields['phone'].label = 'Số điện thoại:'
        self.fields['email'].label = 'Email:'
        self.fields['address'].label = 'Địa chỉ giao hàng:'