from django.urls import path
from dashboard.views import hr_register_employee_page, login_page, dashboard_page, logout_page, payroll_employee_add_salary


urlpatterns = [
    path('dashboard/', dashboard_page),
    path('dashboard/hr-register-employee/', hr_register_employee_page),
    path('dashboard/payroll-employee-add-salary/<str:uuid>/',
         payroll_employee_add_salary),
    path('login/', login_page),
    path('logout/', logout_page)
]
