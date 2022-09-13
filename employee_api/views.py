from asyncio.windows_events import NULL
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import IntegrityError
from dashboard.views import hr_register_employee_function
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class EmployeeListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Employee
        '''
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Employee
        '''
        res = hr_register_employee_function(email)
        if res == "duplicate user":
            return Response("Username is not Unique", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(res, status=status.HTTP_201_CREATED)
