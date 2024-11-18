from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order  # Specify the model to use
        fields = ['customer_name', 'customer_contact', 'quantity', 'product']  # Fields to include in the form
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
            'customer_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer contact'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'product': forms.Select(attrs={'class': 'form-control'}),  # Product will use a dropdown select widget
        }
