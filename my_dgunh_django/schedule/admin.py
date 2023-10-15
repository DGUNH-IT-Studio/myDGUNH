from django.contrib import admin
from .models import term, university_faculty, education_profile, education_program,\
                    university_group, student_schedule, department, teacher, \
                    teacher_schedule
# from scheduleEditor import Schedule


# admin.site.register([Term, University_Faculty, Education_program, Group, Student_schedule])
# admin.site.register([Department, Professor])


@admin.register(term)
class term_admin(admin.ModelAdmin):
    fields = [
        'term_num', 'term_start', 'term_end',
    ]
    list_display = [
        'term_num', 'term_start', 'term_end'
    ]
    list_filer = [
        'term_num', 'term_start', 'term_end'
    ]
    search_fields = [
        'term_num', 'term_start', 'term_end'
    ]
    ordering = [
        'term_start', 'term_end'
    ]


@admin.register(university_faculty)
class university_faculty_admin(admin.ModelAdmin):
    fields = [
        'faculty_full_name', 'faculty_short_name'
    ]
    list_display = [
        'faculty_full_name', 'faculty_short_name'
    ]
    list_filer = [
        'faculty_full_name', 'faculty_short_name'
    ]
    search_fields = [
        'faculty_full_name', 'faculty_short_name'
    ]
    ordering = [
        'faculty_full_name', 'faculty_short_name'
    ]


@admin.register(education_profile)
class education_profile_admin(admin.ModelAdmin):
    fields = [
        'faculty', 'profile'
    ]
    list_display = [
        'faculty', 'profile'
    ]
    list_filter = [
        'faculty', 'profile'
    ]
    search_fields = [
        'faculty', 'profile'
    ]
    ordering = [
        'faculty', 'profile'
    ]


@admin.register(education_program)
class education_program_admin(admin.ModelAdmin):
    fields = [
        'profile', 'education_level', 'education_form',
        'education_program_name'
    ]
    list_display = [ 
        'profile', 'education_level', 'education_form',
        'education_program_name'
    ]
    list_filer = [
        'profile', 'education_level', 'education_form',
        'education_program_name'
    ]
    search_fields = [
        'profile', 'education_level', 'education_form',
        'education_program_name'
    ]
    ordering = [
        'profile', 'education_program_name'
    ]


@admin.register(university_group)
class university_group_admin(admin.ModelAdmin):
    fields = [
        'group_education_program', 'course', 'stream', 'group_num',
        'subgroup_num'
    ]
    list_display = [
        'group_education_program', 'course', 'stream', 'group_num',
        'subgroup_num'
    ]
    list_filer = [
        'group_education_program', 'course', 'stream', 'group_num',
        'subgroup_num'
    ]
    search_fields = [
        'group_education_program', 'course', 'stream', 'group_num',
        'subgroup_num'
    ]
    ordering = [
        'group_education_program', 'course', 'stream', 'group_num',
        'subgroup_num'
    ]


@admin.register(student_schedule)
class student_schedule_admin(admin.ModelAdmin):
    fields = [
        'group', 'term_num', 'date_start', 'date_end', 'schedule_object',
        'date_add', 'lastupdate'
    ]
    list_display = [
        'group', 'term_num', 'date_start', 'date_end', 'schedule_object',
        'date_add', 'lastupdate'
    ]
    list_filer = [
        'group', 'term_num', 'date_start', 'date_end', 'schedule_object',
        'date_add', 'lastupdate'
    ]
    search_fields = [
        'group', 'term_num', 'date_start', 'date_end', 'schedule_object',
        'date_add', 'lastupdate'
    ]
    ordering = [
        'group', 'term_num', 'date_start', 'date_end', 'schedule_object',
        'date_add', 'lastupdate'
    ]


@admin.register(department)
class department_admin(admin.ModelAdmin):
    fields = [
        'department_name', 'subjects'
    ]
    list_display = [
        'department_name', 'subjects'
    ]
    list_filer = [
        'department_name', 'subjects'
    ]
    search_fields = [
        'department_name', 'subjects'
    ]
    ordering = [
        'department_name', 'subjects'
    ]


@admin.register(teacher)
class teacher_admin(admin.ModelAdmin):
    fields = [
        'teacher_department', 'first_name', 'second_name', 'last_name',
        'schedule_view_name'
    ]
    list_display = [
        'teacher_department', 'first_name', 'second_name', 'last_name',
        'schedule_view_name'
    ]
    list_filer = [
        'teacher_department', 'first_name', 'second_name', 'last_name',
        'schedule_view_name'
    ]
    search_fields = [
        'teacher_department', 'first_name', 'second_name', 'last_name',
        'schedule_view_name'
    ]
    ordering = [
        'teacher_department', 'first_name', 'second_name', 'last_name',
        'schedule_view_name'
    ]


@admin.register(teacher_schedule)
class teacher_schedule_admin(admin.ModelAdmin):
    fields = [
        'teacher_info', 'teacher_schedule'
    ]
    list_display = [
        'teacher_info', 'teacher_schedule'
    ]
    list_filer = [
        'teacher_info', 'teacher_schedule'
    ]
    search_fields = [
        'teacher_info', 'teacher_schedule'
    ]
    ordering = [
        'teacher_info', 'teacher_schedule'
    ]


# class ScheduleAdmin(Schedule, admin.ModelAdmin):
#
#     def __init__(self):
#         super().__init__()
#
#
# class ScheduleEventAdmin(admin.ModelAdmin):
#
#     def __int__(self):
#         super().__init__()
#
#     #     # Функция для получения списка всех событий расписания на
#     #     # определенную дату, в определенный день недели для
#     #     # соответствующей недели.
#     #
#     #     from datetime import datetime
#     #
#     #     events = list()
#     #     current_date = None
#     #
#     #     if iso_format_date is None:
#     #         current_date = datetime.today()
#     #     else:
#     #         current_date = datetime.fromisoformat(iso_format_date)
#     #
#     #     weeknum = Week().weeknum
#     #     weekday = Week()[current_date.weekday()]
#     #
#     #     events = schedule[weeknum][weekday]
#     #
#     # def __init__(self, schedule: dict = None, event={}) -> None:
#     #     self.event = event
#     #     self.event_list = self.__eventsparser(schedule) if schedule else [event]
#     #
#     # def __getitem__(self, index: int):
#     #     return self.event_list[index]
#     #
#     #
#     # def delete(self, event: dict):
#     #     self.__init__(event={})
#     #
#     # def update(self, new_values: dict):
#     #     for i in new_values.keys():
#     #         self.event[i] = new_values[i]
#     #     return
