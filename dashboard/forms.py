from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterEmployeeForm(forms.Form):
    email = forms.EmailField()


class EmployeeAddSalary(forms.Form):
    amount = forms.CharField(widget=forms.NumberInput())
