from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def emp_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            employee = EmployeeForm()
        else:
            data = Employee.objects.get(pk=id)
            employee = EmployeeForm(instance = data)
        return render(request, 'emp_form.html', {'employees': employee})
    else:
        if id == 0:
            employee = EmployeeForm(request.POST)
        else:
            data = Employee.objects.get(pk=id)
            employee = EmployeeForm(request.POST, instance=data)
        if employee.is_valid():
            employee.save()
        return redirect('/list')

    return render(request, 'emp_form.html', {'employees': employee})

def emp_delete(request, id=0):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')



def list(request):
    employees = {'employees' : Employee.objects.all()}
    # Select * from employee
    return render(request, 'list.html', employees)