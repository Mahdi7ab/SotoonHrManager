from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from employees.forms import ApplyForm, EditEmployeeForm, EditSalaryForm
from employee_api.serializers import EmployeeSerializer

from .models import Employee, Salary


def employee_apply_page(request, uuid):
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            # update employee
            Employee.objects.update(**form.cleaned_data)
            # update user and set password
            usernameFromEmail = str(email).split('@', 1)[0]
            user = User.objects.get(username=usernameFromEmail)
            user.set_password(password)
            # update username
            user.username = username
            user.save()
            return HttpResponseRedirect("/dashboard/")
    else:
        form = ApplyForm()
        context = {'form': form}
        employee = Employee.objects.get(uuid=uuid)
        email = employee.email
        context['email'] = email
        context['uuid'] = uuid
        # check if register ...
        if employee.name != '':
            context['is_registered'] = True
    return render(request, "employees/apply-form.html", context=context)


def edit_employee_page(request, uuid):
    if request.method == 'POST':
        form = EditEmployeeForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            email = request.POST.get('email')
            context['email'] = email
            # update employee
            Employee.objects.update(**form.cleaned_data)
            return HttpResponseRedirect("/dashboard/")
    else:
        employee = Employee.objects.get(uuid=uuid)
        form = EditEmployeeForm(
            initial={'name': employee.name, 'international_code': employee.international_code, 'birthday': employee.birthday})
        context = {'form': form}
        context['employee'] = employee
        context['uuid'] = uuid
    return render(request, "employees/edit.html", context=context)


def view_salary_page(request, uuid):
    employee = Employee.objects.get(uuid=uuid)
    context = {'employee': employee}
    salaries = Salary.objects.filter(employee_id=employee.id)
    context['salaries'] = salaries
    context['uuid'] = uuid
    return render(request, "employees/salary/view.html", context=context)


def edit_salaries_page(request, uuid):
    employee = Employee.objects.get(uuid=uuid)
    context = {'employee': employee}
    salaries = Salary.objects.filter(employee_id=employee.id)
    context['salaries'] = salaries
    context['uuid'] = uuid
    return render(request, "employees/salary/edit-salaries.html", context=context)


def edit_salary_page(request, uuid, salary_id):
    if request.method == 'POST':
        form = EditSalaryForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            # update employee
            Salary.objects.update(**form.cleaned_data)
            return HttpResponseRedirect("/employee/edit-salaries/"+uuid)
    else:
        employee = Employee.objects.get(uuid=uuid)
        salary = Salary.objects.get(pk=salary_id)
        form = EditSalaryForm(
            initial={'amount': salary.amount})
        context = {'form': form}
        context['employee'] = employee
        context['salary'] = salary
        context['uuid'] = uuid
    return render(request, "employees/salary/edit.html", context=context)


def delete_salary(request, uuid, salary_id):
    try:
        salary = Salary.objects.get(pk=salary_id)
        salary.delete()
        return HttpResponseRedirect("/employee/edit-salaries/"+uuid)
    except:
        return HttpResponseRedirect("/dashboard/")
