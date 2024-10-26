# management_application/employee_management/forms.py
from django import forms
from .models import Employee, Attendance

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'department', 'date_of_joining']  # Adjust fields as necessary
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'})  # Use a date picker for the date field
        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'status']  # Adjust fields as necessary
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # Use a date picker for the date field
        }
