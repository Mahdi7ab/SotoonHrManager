from django import forms

from employees.models import Employee, Salary


class ApplyForm(forms.Form):
    username = forms.CharField()
    name = forms.CharField()
    international_code = forms.CharField()
    birthday = forms.DateField()
    password = forms.CharField(widget=forms.PasswordInput())


class EditEmployeeForm(forms.Form):
    name = forms.CharField()
    international_code = forms.CharField()
    birthday = forms.DateField(widget=forms.DateInput())

    class Meta:
        model = Employee


class EditSalaryForm(forms.Form):
    amount = forms.CharField(widget=forms.NumberInput())

    class Meta:
        model = Salary
