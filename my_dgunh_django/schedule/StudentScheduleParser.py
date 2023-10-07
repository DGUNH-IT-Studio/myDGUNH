from .models import Term, University_Faculty, \
                    Education_program, Group, Student_schedule
from professor_schedule.models import Department, Professor


def main():
    all_schedules = list(Student_schedule.objects.all())
    all_teachers = list(Professor.objects.all())

    for i in all_teachers:
        schedule_view_name = str(i.SecondName).capitalize() + ' ' + \
                             str(i.FirstName)[0].upper() + '.' + \
                             str(i.LastName)[0].upper() + '.'
        lessons = list(i.Subjects)
        for j in all_schedules:
            current_schedule = dict(j.scheduleFile)
            # написать перебор элементов расписания для поиска eventa который преподаватель преподает для занесения в расписание преподавателя
            # написать класс для обработки вносимых в расписание преподавателя предметов

    return 0

if __name__ == "__main__":
    main()
