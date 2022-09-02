from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     HRMANAGER = 1
#     PAYROLLMANAGER = 2
#     EMPLOYEE = 3

#     ROLE_CHOICES = (
#         (HRMANAGER, 'HrManager'),
#         (PAYROLLMANAGER, 'PayrollManager'),
#         (EMPLOYEE, 'Employee'),
#     )
#     role = models.PositiveSmallIntegerField(
#         choices=ROLE_CHOICES, blank=True, null=True)


class Salary(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    amount = models.IntegerField()


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(blank=True, max_length=50)
    username = models.CharField(blank=True, max_length=50, unique=True)
    international_code = models.CharField(blank=True, max_length=10)
    birthday = models.DateField(blank=True, null=True)
    password = models.CharField(blank=True, max_length=50)
    uuid = models.UUIDField(null=True, blank=True)
