from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class TermViewSets(viewsets.ModelViewSet):
    queryset = term.objects.all()
    serializer_class = TermSerializer


class FacultyViewSets(viewsets.ModelViewSet):
    queryset = university_faculty.objects.all() 
    serializer_class = FacultySerializer


class EducationProfileViewSets(viewsets.ModelViewSet):
    queryset = education_profile.objects.all()
    serializer_class = EducationProfileSerializer


class EducationProgramViewSets(viewsets.ModelViewSet):
    queryset = education_program.objects.all()
    serializer_class = EducationProgramSerializer


class UniversityGroupViewSets(viewsets.ModelViewSet):
    queryset = university_group.objects.all()
    serializer_class = UniversityGroupSerializer


class ScheduleViewSets(viewsets.ModelViewSet):
    queryset = student_schedule.objects.all()
    serializer_class = StudentScheduleSerializer


class DepartmentViewSets(viewsets.ModelViewSet):
    queryset = department.objects.all()
    serializer_class = DepartmentSerializer


class TeacherViewSets(viewsets.ModelViewSet):
    queryset = teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherScheduleViewSets(viewsets.ModelViewSet):
    queryset = teacher_schedule.objects.all()
    serializer_class = TeacherScheduleSerializer

