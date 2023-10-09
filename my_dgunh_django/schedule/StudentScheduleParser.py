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
                condition = teacher == i['presenter'] and i['title'] in subjects
                if teacher == i['presenter'] and i['title'] in subjects:
                    # print(f'Week: {w+1}')
                    # print(f'Day of the week: {wd}')
                    # print(f'Class num: {i["num"]}')
                    # print()
                    teachers_events.append(
                        [
                            {
                                "week": str(w),
                                "weekday": str(wd)
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
        if teachers_events == []:
            return teachers_events
    return teachers_events


def main():
    all_schedules = list(Student_schedule.objects.all())
    all_teachers = list(Professor.objects.all())

    for i in all_teachers:
        schedule_view_name = str(i.SecondName).capitalize() + ' ' + \
                             str(i.FirstName)[0].upper() + '.' + \
                             str(i.LastName)[0].upper() + '.'
        lessons = [
            # достать список предметов преподавателя через его кафедру
        ]
        for j in all_schedules:
            found_subjects = schedule_parser(j, i, lessons)
            for subject in found_subjects:
                if subject[1]["type"] in lessons:
                    # teacher_schedule = i.Schedule
                    # teacher_schedule[subject[0]["week"]][subject[0]["weekday"]].add(subject[1])
                    pass

    return 0

if __name__ == "__main__":
    main()

