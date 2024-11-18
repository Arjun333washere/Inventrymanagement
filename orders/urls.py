from django.urls import path
from .views import *

urlpatterns = [
   path('manage_ord',OrderManageView.as_view(),name='orders_manage'),

   path('',OrderView.as_view(),name='orders'),

   path('orders/create/', OrderCreateView.as_view(), name='order_create'),

   path('<int:pk>/edit',EditOrderView.as_view(),name='edit_order'),

   path('<int:pk>/delete',DeleteOrderView.as_view(),name='delete_orders')
]