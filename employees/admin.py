from django.contrib import admin

from .models import Employee, Salary


class SalaryInlineAdmin(admin.StackedInline):
    model = Salary
    fields = ['amount']
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'email', 'uuid']
    search_fields = ['username']
    inlines = [SalaryInlineAdmin]
