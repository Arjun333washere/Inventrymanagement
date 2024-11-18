from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.urls import reverse_lazy

from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from .models import *
from .forms import ProductForm,SupplierForm,StockForm
from accounts.mixins import RoleRequiredMixin


class InventoryView(RoleRequiredMixin,TemplateView):
    allowed_roles = ['Manager','Admin']
    template_name='inventory/inventory.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['total_students'] = Student.objects.all().count()
        context['total_products'] = Product.objects.all().count()
        context['total_supplier'] = Supplier.objects.all().count()
        return context

class ProductCreateView(RoleRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/inventory/create_product.html'
    success_url = reverse_lazy('inventory_manage')  # Redirect after successful creation
    allowed_roles = ['Manager', 'Admin']  # Only these roles can access this view



class EditProductView(RoleRequiredMixin, UpdateView):
    allowed_roles = ['Manager', 'Admin']
    model = Product
    form_class = ProductForm
    template_name = 'inventory/inventory/edit-products.html'
    success_url = reverse_lazy('inventory_manage')


class DeleteProductView(RoleRequiredMixin,DeleteView):
    allowed_roles = ['Manager', 'Admin']
    model = Product
    def post(self, request, pk):
        std = get_object_or_404(Product, pk=pk)
        std.delete()
        return redirect('inventory_manage')
    
class InventoryManageView(RoleRequiredMixin,ListView):
    allowed_roles = ['Manager','Admin']
    template_name='inventory/inventory/inventory_manage.html'
    model = Product
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classlist'] = Product.objects.all()
        return context
    

#supplier details

class SupplierCreateView(RoleRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventory/inventory/create_supplier.html'
    success_url = reverse_lazy('supplier_manage')  # Redirect after successful creation
    allowed_roles = ['Manager', 'Admin']  # Only these roles can access this view



class EditSupplierView(RoleRequiredMixin, UpdateView):
    allowed_roles = ['Manager', 'Admin']
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventory/inventory/edit-supplier.html'
    success_url = reverse_lazy('supplier_manage')


class DeleteSupplierView(RoleRequiredMixin,DeleteView):
    allowed_roles = ['Manager', 'Admin']
    model = Supplier
    def post(self, request, pk):
        std = get_object_or_404(Product, pk=pk)
        std.delete()
        return redirect('supplier_manage')

class SupplierManageView(RoleRequiredMixin,ListView):
    allowed_roles = ['Manager','Admin']
    template_name='inventory/inventory/supplier_manage.html'
    model = Supplier
    context_object_name = 'suppliers'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classlist'] = Supplier.objects.all()
        return context
    


#stock info 


class StockManageView(RoleRequiredMixin,ListView):
    allowed_roles = ['Manager','Admin']
    template_name='inventory/inventory/stock_manage.html'
    model = Stock
    context_object_name = 'stocks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classlist'] = Stock.objects.all()
        return context
    

class StockCreateView(RoleRequiredMixin, CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'inventory/inventory/create_stock.html'
    success_url = reverse_lazy('stock_manage')  # Redirect after successful creation
    allowed_roles = ['Manager', 'Admin']  # Only these roles can access this view



class EditStockView(RoleRequiredMixin, UpdateView):
    allowed_roles = ['Manager', 'Admin']
    model = Stock
    form_class = StockForm
    template_name = 'inventory/inventory/edit-stock.html'
    success_url = reverse_lazy('stock_manage')


class DeleteStockView(RoleRequiredMixin,DeleteView):
    allowed_roles = ['Manager', 'Admin']
    model = Stock
    def post(self, request, pk):
        std = get_object_or_404(Product, pk=pk)
        std.delete()
        return redirect('stock_manage')