from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer
# Create your views here.

class StudentView(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = (StudentSerializer(students, many=True))
        return Response({"message":serializer.data}, status=200)
        

    def post(self, request):
        student = request.data
        serializer = StudentSerializer(data=student)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"Student Created"}, status=200)
        else:
            return Response({"Message":"Invalid Student Record"}, status=400)