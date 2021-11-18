from django.shortcuts import render
from teacher.models import Teacher
from student.models import Student

from .serializers import TeacherListSerializer, TeacherDetailSerializer, StudentListSerializer, StudentDetailSerializer
from rest_framework import generics


"""Teachers API View"""


class TeacherCreateView(generics.CreateAPIView):
    serializer_class = TeacherDetailSerializer


class TeacherListView(generics.ListAPIView):
    serializer_class = TeacherListSerializer
    queryset = Teacher.objects.all()


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherDetailSerializer
    queryset = Teacher.objects.all()


"""Students API View"""


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentDetailSerializer


class StudentListView(generics.ListAPIView):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all()


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()
