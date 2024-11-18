from django.urls import path
from . import views

urlpatterns = [
    path('',views.AdminDashBoardView.as_view(),name='admin_dashboard'),
    path('manage_staff',views.ManageStaffView.as_view(),name='manage_staff'),
    path('manage_manager',views.ManageManagerView.as_view(),name='manage_manager'),
    path('search_users', views.UserSearchView.as_view(), name='search_users'),
]