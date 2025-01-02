from django.urls import path
from . import views
app_name = 'hr'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('employee/add/', views.EmployeeCreate.as_view(), name='employee-add'),
    path('employee/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee-delete'),
]
