from django.contrib import admin
from .models import Term, University_Faculty, Education_program,\
                    Group, Student_schedule


admin.site.register([Term, University_Faculty, Education_program, Group, Student_schedule])


# from scheduleEditor import Schedule


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
#     #     return events
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
