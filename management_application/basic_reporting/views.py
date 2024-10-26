from django.shortcuts import render
from employee_management.models import Employee
from django.db.models import Count

def department_report_view(request):
    department_counts = Employee.objects.values('department').annotate(count=Count('id'))
    return render(request, 'basic_reporting/department_report.html', {'department_counts': department_counts})
