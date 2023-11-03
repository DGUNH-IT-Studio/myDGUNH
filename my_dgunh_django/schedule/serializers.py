from rest_framework import serializers
from rest_framework.fields import empty
from .models import term, university_faculty, teacher_schedule, \
                    student_schedule, education_profile, \
                    education_program, university_group, \
                    department, teacher


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = term
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = university_faculty
        fields = '__all__'

class EducationProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = education_profile
        fields = '__all__'


class EducationProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = education_program
        fields = '__all__'


class UniversityGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = university_group 
        fields = '__all__'


class StudentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_schedule
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'


class TeacherScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher_schedule
        fields = '__all__'
