from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.mixins import RoleRequiredMixin
from accounts.models import User
from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
from django.views.generic import View

class AdminDashBoardView(RoleRequiredMixin, TemplateView):
    allowed_roles = ['Admin']
    template_name = 'admin_dashboard/admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['librarian_count'] = User.objects.filter(role='Manager').count()#change
        context['officestaff_count'] = User.objects.filter(role='Sales Staff').count()
        context['admin_count'] = User.objects.filter(role='Admin').count()
        return context

class ManageStaffView(RoleRequiredMixin, TemplateView):
    allowed_roles = ['Admin']
    template_name = 'admin_dashboard/manage_staff.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["staffs"] = User.objects.filter(role='Sales Staff')
        return context

class ManageManagerView(RoleRequiredMixin,TemplateView):
    allowed_roles = ['Admin']
    template_name = 'admin_dashboard/manage_manager.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['librarians'] = User.objects.filter(role='Manager')
        return context


class UserSearchView(RoleRequiredMixin,View):
    allowed_roles = ['Admin']
    def get(self, request):
        query = request.GET.get('q', '')
        role = request.GET.get('role', '')
        if query:
            users = User.objects.filter(role=role, username__icontains=query)
        else:
            users = User.objects.filter(role=role)

        users_list = list(users.values('id', 'username', 'email'))
        return JsonResponse({'users': users_list})