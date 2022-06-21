from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Students
from .serializers import StudentSerializer

# Create your views here.

class StudentsView(APIView):
    def get(self, request):
        student = Students.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)