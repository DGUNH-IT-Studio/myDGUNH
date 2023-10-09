from .models import Term, University_Faculty, \
                    Education_program, Group, Student_schedule
from professor_schedule.models import Department, Professor, Professor_schedule
from .scheduleEditor import Schedule


def get_group_info(group_schedule:Student_schedule = None):
    group = Group.objects.get(id=group_schedule.scheduleID)
    groupinfo = {
        "faculty": str(University_Faculty.objects.get(id=Education_program.objects.get(id=group.EduProgram).Faculty).faculty_short_name),
        "profile": str(Education_program.objects.get(id=group.EduProgram).EduProgram),
        "educationform": str(Education_program.objects.get(id=group.EduProgram).Edu_form),
        "course": str(group.Course),
        "stream": str(group.Stream),
        "group": str(group.GroupNum)
    }
    return groupinfo


def schedule_parser(Group_schedule:Student_schedule, teacher:str, subjects:list[str]):
    teacher_events = list()
    schedule = list(Group_schedule.scheduleFile)
    for week in range(2):
        for weekday in schedule[week].keys():
            for event in schedule[week][weekday]:
                if event["presenter"] == teacher and event["title"] in subjects:
                    event["groupinfo"] = get_group_info(Group_schedule)
                    teacher_events.append(
                        [
                            {
                                "week": week,
                                "weekday": weekday
                            },
                            event
                        ]
                    )
    if teacher_events == []:
        return teacher_events
    return teacher_events


def main():
    all_schedules = list(Student_schedule.objects.all())
    all_teachers = list(Professor.objects.all())

    for teacher in all_teachers:
        schedule_view_name = teacher.ScheduleViewName
        lessons = list(Department.objects.filter(professor = teacher.Professor_Department))
        for schedule in all_schedules:
            found_subjects = schedule_parser(schedule, schedule_view_name, lessons)
            for subject in found_subjects:
                professor_schedule = list(Professor_schedule.objects.get(ProfessorID=teacher.pk))
                professor_schedule = Schedule(professor_schedule)
                professor_schedule.paste_event(subject[0]["week"], subject[0]["weekday"], subject[1])
    return 0

if __name__ == "__main__":
    main()
