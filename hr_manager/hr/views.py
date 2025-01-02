from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
from datetime import date
from datetime import timedelta

class DashboardView(ListView):
    model = Employee
    template_name = 'hr/dashboard.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expiring_soon'] = Employee.objects.filter(
            contract_end__lte=date.today() + timedelta(days=30)
        )
        return context

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'position', 'email', 'date_joined', 'contract_length', 'contract_end', 'role']
    success_url = reverse_lazy('dashboard')

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'position', 'email', 'date_joined', 'contract_length', 'contract_end', 'role']
    success_url = reverse_lazy('dashboard')

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('dashboard')
