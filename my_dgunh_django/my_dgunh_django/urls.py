"""
URL configuration for my_dgunh_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from schedule.views import *
from rest_framework import routers

BASE_ENDPOINT = ''

term_router = routers.SimpleRouter()
term_router.register(r'terms', TermViewSets)

faculty_router = routers.SimpleRouter()
faculty_router.register(r'faculties', FacultyViewSets)

education_profile_router = routers.SimpleRouter()
education_profile_router.register(r'eduprofiles', EducationProfileViewSets)

education_program_router = routers.SimpleRouter()
education_program_router.register(r'eduprograms', EducationProgramViewSets)

university_group_router = routers.SimpleRouter()
university_group_router.register(r'groups', UniversityGroupViewSets)

student_schedule_router = routers.SimpleRouter()
student_schedule_router.register(r'student_schedules', ScheduleViewSets)

department_router = routers.SimpleRouter()
department_router.register(r'departments', DepartmentViewSets)

teacher_router = routers.SimpleRouter()
teacher_router.register(r'teachers', TeacherViewSets)

teacher_schedule_router = routers.SimpleRouter()
teacher_schedule_router.register(r'teacher_schedules', TeacherScheduleViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_ENDPOINT, include(term_router.urls)),
    path(BASE_ENDPOINT, include(faculty_router.urls)),  # faculty
    path(BASE_ENDPOINT, include(education_profile_router.urls)),  # profile
    path(BASE_ENDPOINT, include(education_program_router.urls)),  # program
    path(BASE_ENDPOINT, include(university_group_router.urls)),  # group
    path(BASE_ENDPOINT + 'schedule/', include(student_schedule_router.urls)),
    path(BASE_ENDPOINT, include(department_router.urls)),  # dep
    path(BASE_ENDPOINT, include(teacher_router.urls)),  # teacher
    path(BASE_ENDPOINT + 'schedule/', include(teacher_schedule_router.urls)),  # teacher schedule
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
