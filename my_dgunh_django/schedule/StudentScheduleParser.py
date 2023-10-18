from .models import term, university_faculty, education_profile, \
                    education_program, university_group, \
                    student_schedule, department, teacher, teacher_schedule, \
                    DEFAULT_PROFESSOR_SCHEDULE
from .scheduleEditor import Schedule


def get_group_info(group_schedule: student_schedule):
    group_info = dict()
    group_object = university_group.objects.get(
        filter=university_group.pk == student_schedule.objects.get(
            filter=student_schedule.schedule_object == group_schedule
        ).group
    )
    group_faculty = 0
    edu_profile = 0
    edu_form = 0
    group_info["faculty"] = str(group_faculty)
    group_info["profile"] = str(edu_profile)
    group_info["education_form"] = str(edu_form)
    group_info["stream"] = str(group_object.stream)
    group_info["course"] = str(group_object.group_course)
    group_info["group"] = str(group_object.group_num)
    return 0


def schedule_object_parser(group_schedule: list[dict], schedule_view_teacher_name: str, group_info: dict):
    teacher_schedule = DEFAULT_PROFESSOR_SCHEDULE
    for week_num in range(2):
        for weekday in group_schedule[week_num].keys():
            for event in group_schedule[week_num][weekday]:
                condition = bool()
                if condition:
                    new_teacher_event = event
                    new_teacher_event["groupinfo"] = group_info
                    teacher_schedule[week_num][weekday].append()
    return 0


def main():
    return 0

if __name__ == "__main__":
    main()
