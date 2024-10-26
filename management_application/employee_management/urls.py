from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add_employee/', views.add_employee_view, name='add_employee_view'),  # View to add an employee
    path('list_employees/', views.list_employees_view, name='list_employees_view'),  # View to list all employees
    path('employee/<int:employee_id>/', views.employee_detail_view, name='employee_detail'),  # View for employee detail
    path('mark_attendance/<int:employee_id>/', views.mark_attendance_view, name='mark_attendance_view'),
    path('attendance/<int:employee_id>/', views.attendance_details_view, name='attendance_details_view'),  # View to mark attendance for an employee
]
