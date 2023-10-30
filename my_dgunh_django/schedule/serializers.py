from rest_framework import serializers
from rest_framework.fields import empty
from .models import term, university_faculty, teacher_schedule, \
                    student_schedule, education_profile, \
                    education_program, university_group, \
                    department, teacher


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = term
        fields = (
            'term_num', 'term_start', 'term_end'
        )


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = university_faculty
        fields = (
            'faculty_full_name', 'faculty_short_name'
        )


class EducationProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = education_profile
        fields = (
            'faculty', ## foreign key
            'profile'
        )


class EducationProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = education_program
        fields = (
            'profile', ## foreign key,
            'education_level', 'education_form', 'education_program_name'
        )


class UniversityGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = university_group 
        fields = (
            'group_education_program', ## foreign key
            'course', 'stream', 'group_num', 'subgroup_num'
        )


class StudentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_schedule
        fields = (
            'group', ## foreign key
            'term_num', ## foreign key
            'date_start', 'date_end', 'schedule_object'
        )


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = (
            'department_name', 'subjects'
        )


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = (
            'teacher_department', ## foreign key
            'first_name', 'second_name', 'last_name', 'schedule_view_name'
        )


class TeacherScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher_schedule
        fields = (
            'teacher_info', ## foreign key
            'teacher_schedule'
        )
