from django.urls import path
from .views import *

urlpatterns = [
    path('products/create/', ProductCreateView.as_view(), name='product_create'),

    path('',InventoryView.as_view(),name='manager'),

    path('manage',InventoryManageView.as_view(),name='inventory_manage'),   

    path('<int:pk>/edit',EditProductView.as_view(),name='edit_product'), 

    path('<int:pk>/delete',DeleteProductView.as_view(),name='delete_product'),
    #supplier

    path('manage_sup',SupplierManageView.as_view(),name='supplier_manage'),

    path('supplier/create/', SupplierCreateView.as_view(), name='supplier_create'),

    path('<int:pk>/edit_sup',EditSupplierView.as_view(),name='edit_supplier'),

    path('<int:pk>/delete_sup',DeleteSupplierView.as_view(),name='delete_supplier'),
#stock
    path('manage_stock',StockManageView.as_view(),name='stock_manage'),

    path('stock/create/', StockCreateView.as_view(), name='stock_create'),

    path('<int:pk>/edit_stk',EditStockView.as_view(),name='edit_stock'),

    path('<int:pk>/delete_stk',DeleteStockView.as_view(),name='delete_stock'),
]