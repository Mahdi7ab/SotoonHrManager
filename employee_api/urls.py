from django.urls import path

from employee_api.views import EmployeeListApiView

urlpatterns = [
    path('employee_api', EmployeeListApiView.as_view()),
]
