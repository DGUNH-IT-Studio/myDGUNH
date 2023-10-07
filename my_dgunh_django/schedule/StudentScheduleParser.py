# написать перебор элементов расписания для поиска eventa который преподаватель преподает для занесения в расписание преподавателя
# написать класс для обработки вносимых в расписание преподавателя предметов

from .models import Term, University_Faculty, \
                    Education_program, Group, Student_schedule
from professor_schedule.models import Department, Professor

def schedule_parser(schedule:list[dict], teacher:str, subjects:list):
    teachers_events = list()
    for w in range(2):
        for wd in list(schedule[w].keys()):
            for i in schedule[w][wd]:
                if teacher == i['presenter'] and i['title'] in subjects:
                    # print(f'Week: {w+1}')
                    # print(f'Day of the week: {wd}')
                    # print(f'Class num: {i["num"]}')
                    # print()
                    teachers_events.append(
                        [
                            {
                                "week": w,
                                "weekday": wd
                            },
                            {
                                "num": i["num"],
                                "type": i["type"],
                                "room": i["room"],
                                "building": i["building"],
                                "notes": i["notes"],
                                "links": i["links"]
                            }
                        ]
                    )
    return teachers_events


def main():
    all_schedules = list(Student_schedule.objects.all())
    all_teachers = list(Professor.objects.all())

    for i in all_teachers:
        schedule_view_name = str(i.SecondName).capitalize() + ' ' + \
                             str(i.FirstName)[0].upper() + '.' + \
                             str(i.LastName)[0].upper() + '.'
        lessons = list(i.Subjects)
        for j in all_schedules:
            schedule_parser(j, i)

    return 0

if __name__ == "__main__":
    main()
