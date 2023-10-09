from .models import Term, University_Faculty, \
                    Education_program, Group, Student_schedule
from professor_schedule.models import Department, Professor, Professor_schedule
from .scheduleEditor import Schedule


def get_group_info(group_schedule:Student_schedule = None):
    group = Group.objects.filter(group_schedule.pk)
    return 0


def schedule_parser(Group_schedule:Student_schedule, teacher:str, subjects:list[str]):
    teacher_events = list()
    schedule = list(Group_schedule.scheduleFile)
    for week in range(2):
        for weekday in schedule[week].keys():
            for event in schedule[week][weekday]:
                if event["presenter"] == teacher and event["title"] in subjects:
                    groupinfo = Group.objects.get(id=Group_schedule.scheduleID)
                    event["groupinfo"] = {
                        # "faculty": "",
		                # "profile": "",
		                # "educationform": "",
		                # "course": "",
		                # "stream": "",
		                # "group": ""
                        "faculty": str(University_Faculty.objects.get(id=Education_program.objects.get(id=groupinfo.EduProgram).Faculty).faculty_short_name),
		                "profile": str(Education_program.objects.get(id=groupinfo.EduProgram).EduProgram),
		                "educationform": str(Education_program.objects.get(id=groupinfo.EduProgram).Edu_form),
		                "course": str(groupinfo.Course),
		                "stream": str(groupinfo.Stream),
		                "group": str(groupinfo.GroupNum)
                    }
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
            found_subjects = schedule_parser(list(schedule.scheduleFile), schedule_view_name, lessons)
            for subject in found_subjects:
                pass

    return 0

if __name__ == "__main__":
    main()
