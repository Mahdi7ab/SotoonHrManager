from django.urls import path

from .views import delete_salary, employee_apply_page, edit_employee_page, view_salary_page, edit_salary_page, edit_salaries_page

urlpatterns = [
    path('employees/apply-form/<str:uuid>', employee_apply_page),
    path('employee/edit-employee/<str:uuid>', edit_employee_page),
    path('employee/view-salary/<str:uuid>', view_salary_page),
    path('employee/edit-salaries/<str:uuid>', edit_salaries_page),
    path('employee/edit-salary/<str:uuid>/<int:salary_id>', edit_salary_page),
    path('employee/delete-salary/<str:uuid>/<int:salary_id>', delete_salary),

]
