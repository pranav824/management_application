from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Attendance
from django.http import HttpResponse
from django.utils import timezone
from .forms import AttendanceForm

def home(request):
    '''This method is used render to the home page.'''

    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'employee_management/home.html', {'employees': employees})


def add_employee_view(request):
    '''This method is used to add the details of a new employee into the database.'''

    if request.method == 'POST':
        name = request.POST['name']
        designation = request.POST['designation']
        department = request.POST['department']
        date_of_joining = request.POST['date_of_joining']
        Employee.objects.create(
            name=name,
            designation=designation,
            department=department,
            date_of_joining=date_of_joining
        )
        return redirect('list_employees_view')
    return render(request, 'employee_management/add_employee.html')


def list_employees_view(request):

    '''This method is used to list out the employee which was added previously.'''

    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'employee_management/list_employees.html', {'employees': employees})


def employee_detail_view(request, employee_id):

    '''This method is used to get the employee details which are present in the database.'''

    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employee_management/employee_detail.html', {'employee': employee})


def attendance_details_view(request, employee_id):

    '''This method is used to get the attendance detail of an employee by using the id of the employee.'''

    employee = Employee.objects.get(id=employee_id)
    attendance_records = Attendance.objects.filter(employee=employee)
    return render(request, 'employee_management/attendance_details.html', {
        'employee': employee,
        'attendance_records': attendance_records,
    })



def mark_attendance_view(request, employee_id):

    '''This method is used to mark the attendance of an employee for a specific date.'''

    employee = Employee.objects.get(id=employee_id)  # Get the employee object
    if request.method == 'POST':
        form = AttendanceForm(request.POST)  # Create a form instance with the posted data
        if form.is_valid():
            attendance = form.save(commit=False)  # Create an Attendance instance but don’t save yet
            attendance.employee = employee  # Assign the employee to the attendance record
            attendance.date = timezone.now().date()  # Set today's date or choose a specific date
            attendance.save()  # Save the attendance record
            return redirect('list_employees_view')  # Redirect to the list of employees after saving
    else:
        form = AttendanceForm()  # Create an empty form for GET requests
    
    return render(request, 'employee_management/mark_attendance.html', {
        'form': form,
        'employee': employee
    })