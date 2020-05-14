from django import forms
from .models import Item, Contact


PAYMENT_CHOICES = (
    ('S', 'COD'),
)
class Formsize(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('size',)



class CheckoutForm(forms.Form):
    shipping_name    = forms.CharField(required=True, max_length=100)
    shipping_address = forms.CharField(required=True)
    shipping_address2 = forms.CharField(required=False)
    shipping_phone_number = forms.CharField(required=True)
    save_info = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    use_default_shippinging_address = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)



class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','address','phone_number','email','informations',)
