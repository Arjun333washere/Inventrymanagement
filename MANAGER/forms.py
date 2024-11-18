from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # Specify the model to use
        fields = ['name', 'description', 'price']  # Fields to include in the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
        }



#suppler

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier  # Specify the model to use
        fields = ['name','contact_info']  # Fields to include in the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter supplier name'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        }


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock  # Specify the model to use
        fields = ['product','quantity']  # Fields to include in the form
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        }