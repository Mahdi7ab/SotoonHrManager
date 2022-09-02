from multiprocessing import context
from tokenize import group
from uuid import uuid4
from django.shortcuts import render
from dashboard.forms import EmployeeAddSalary, LoginForm,  RegisterEmployeeForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from employees.models import Employee, Salary


def login_page(request):  # login form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # logout(request)
            user = authenticate(username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/dashboard/", {'user': user})
            else:
                return render(request, "dashboard/login.html", {'error': 'user is not exist'})
    else:
        # check if loged in redirect to dashboard
        if request.user.is_authenticated:
            return HttpResponseRedirect("/dashboard/")
        form = LoginForm()
    return render(request, "dashboard/login.html", {'form': form})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/login/")


# Dashboard home page
def dashboard_page(request):
    user = request.user
    username = user.email.split('@', 1)[0]
    context = {'user': user}
    group = user.groups.first()
    context['group'] = str(group)
    if str(group) == 'HrManagers':
        context['employees'] = Employee.objects.all()
    elif str(group) == 'PayrollManagers':
        context['employees'] = Employee.objects.all()
    else:
        context['employee'] = Employee.objects.get(username=username)
    return render(request, "dashboard/dashboard.html", context=context)


# HR Manager - Register Employee
def hr_register_employee(email):
    username = email.split('@', 1)[0]
    form = RegisterEmployeeForm()
    user, created = User.objects.get_or_create(username=username, email=email)
    if created:
        uuid = uuid4()
        # register employee
        Employee.objects.create(email=email, user=user, uuid=uuid)
        return render(None, "dashboard/hr-register-employee.html", {'form': form, 'uuid': uuid})
    else:
        return render(None, "dashboard/hr-register-employee.html", {'form': form, 'error': "duplicate user"})


def hr_register_employee_page(request):
    if request.method == 'POST':
        form = RegisterEmployeeForm(request.POST)
        if form.is_valid():
            return hr_register_employee(form.cleaned_data.get('email'))
    else:
        form = RegisterEmployeeForm()
    return render(request, "dashboard/hr-register-employee.html", {'form': form})


def payroll_employee_add_salary(request, uuid):
    if request.method == 'POST':
        form = EmployeeAddSalary(request.POST)
        if form.is_valid():
            employee = Employee.objects.get(uuid=uuid)
            Salary.objects.create(employee_id=employee.id, **form.cleaned_data)
        return HttpResponseRedirect("/employee/edit-salaries/"+uuid)
    else:
        form = EmployeeAddSalary()
    return render(request, "dashboard/payroll-employee-add-salary.html", {'form': form, 'uuid': uuid})
