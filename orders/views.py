from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.urls import reverse_lazy

from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from .models import *
from .forms import *
from accounts.mixins import RoleRequiredMixin


# Create your views here.
class OrderManageView(RoleRequiredMixin,ListView):
    allowed_roles = ['Sales Staff','Admin']
    template_name='orders/order_manage.html'
    model = Order
    context_object_name = 'orders'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classlist'] = Order.objects.all()
        return context
    

class OrderView(RoleRequiredMixin,TemplateView):
    allowed_roles = ['Sales Staff','Admin']
    template_name='orders.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['total_students'] = Student.objects.all().count()
        #context['total_products'] = Product.objects.all().count()
        context['total_orders'] = Order.objects.all().count()
        return context

class OrderCreateView(RoleRequiredMixin, CreateView):
    model = Product
    form_class = OrderForm
    template_name = 'orders/create_orders.html'
    success_url = reverse_lazy('orders_manage')  # Redirect after successful creation
    allowed_roles = ['Sales Staff', 'Admin']  # Only these roles can access this view

class EditOrderView(RoleRequiredMixin, UpdateView):
    allowed_roles = ['Sales Staff', 'Admin']
    model = Order
    form_class = OrderForm
    template_name = 'orders/edit-orders.html'
    success_url = reverse_lazy('orders_manage')

class DeleteOrderView(RoleRequiredMixin,DeleteView):
    allowed_roles = ['Sales Staff', 'Admin']
    model = Order
    def post(self, request, pk):
        std = get_object_or_404(Order, pk=pk)
        std.delete()
        return redirect('orders_manage')
    
