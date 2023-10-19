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


# Фукнция для обнаружения тезок
def catch_same():
    teachers = teacher.objects.all()
    teachers_names = [[i.second_name, i.first_name, i.last_name] for i in teachers]
    for i in range(len(teachers) - 1):
        for j in range(i+1, len(teachers)):
            if teachers_names[i] == teachers_names[j]:
                print(teachers[i])
                print(teachers[i].teacher_department)
                print(teachers[j])
                print(teachers[j].teacher_department)
                print()


# create default schedule for each teacher
def create_teacher_default_schedule():
    DEFAULT_PROFESSOR_SCHEDULE = [{"Monday": [],"Tuesday": [],"Wednsday": [],"Thursday": [],"Friday": [],"Saturday": []},{"Monday": [],"Tuesday": [],"Wednsday": [],"Thursday": [],"Friday": [],"Saturday": []}]
    for i in list(teacher.objects.all()):
        teacher_schedule.objects.get_or_create(teacher_info=i, teacher_schedule=DEFAULT_PROFESSOR_SCHEDULE)


def set_each_teacher_schedule_default():
    DEFAULT_PROFESSOR_SCHEDULE = [{"Monday": [],"Tuesday": [],"Wednsday": [],"Thursday": [],"Friday": [],"Saturday": []},{"Monday": [],"Tuesday": [],"Wednsday": [],"Thursday": [],"Friday": [],"Saturday": []}]
    for i in list(teacher_schedule.objects.all()):
        i.teacher_schedule = DEFAULT_PROFESSOR_SCHEDULE
        i.save()


def set_schedule_view_names():
    for i in list(teacher.objects.all()):
        if i.schedule_view_name is None:
            i.schedule_view_name = str(i.second_name).capitalize() + ' ' + str(i.first_name)[0].upper() + '.' + str(i.last_name)[0].upper() + '.'
            i.save()
            print("Done")



# get_teacher_schedule_from_student_schedule 
def teacher_schedule_generator():
    set_each_teacher_schedule_default()
    for i in student_schedule.objects.all():
        schedule_data = list(i.schedule_object)
        for week in range(2):
            for weekday in schedule_data[week].keys():
                for event in schedule_data[week][weekday]:
                    presenter = event["presenter"]
                    new_event = dict(event)
                    new_event["group_info"] = str(i.group)
                    try:
                        cteacher = teacher.objects.get(schedule_view_name=presenter)
                        schedule_of_teacher = teacher_schedule.objects.get(teacher_info=cteacher)
                        tsc = list(schedule_of_teacher.teacher_schedule)
                        tsc[week][weekday].append(new_event)
                        schedule_of_teacher.teacher_schedule = tsc
                        schedule_of_teacher.save()
                    except:
                        print(f"Not found {presenter}")


def main():
    return 0

if __name__ == "__main__":
    main()
