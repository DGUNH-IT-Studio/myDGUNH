from .models import Term, University_Faculty, \
                    Education_program, Group, Student_schedule
from professor_schedule.models import Department, Professor


def main():
    import json
    all_schedules = Student_schedule.objects.all()
    all_teachers = Professor.objects.all()

    

    return 0

if __name__ == "__main__":
    main()
