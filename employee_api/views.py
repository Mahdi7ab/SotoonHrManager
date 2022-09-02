from uuid import uuid4
from django.contrib.auth.models import User
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
        email = request.data.get('email')
        data = {
            'email': email,
        }
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            username = email.split('@', 1)[0]
            user = User.objects.create(
                username=username, email=email)
            uuid = uuid4()
            Employee.objects.create(email=email, user=user, uuid=uuid)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
