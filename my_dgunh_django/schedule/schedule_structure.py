from schedule.models import *

STRUCTURE = {
    "student": {

    },
    "professor": {

    }
}

def define_structure():
    try:
        faculties = university_faculty.objects.all()
    except:
        print("Error 1")
        raise
    for f in faculties:
        STRUCTURE["student"][str(f.faculty_short_name)] = {}
        try:
            education_profiles = education_profile.objects.get(faculty=f)
        except:
            print("Error 2")
            raise
        for p in education_profiles:
            STRUCTURE["student"][str(f.faculty_short_name)][str(p.profile)] = {}
            try:
                education_programs = education_program.objects.get_queryset(profile=p)
            except:
                print("Error 3")
                raise
            for e in education_programs:
                STRUCTURE["student"][str(f.faculty_short_name)][str(p.profile)][str(e.education_program_name)] = [str(g) for g in university_group.objects.get_queryset(group_education_program=e)]


def main():
    define_structure()
    print(STRUCTURE)

if __name__=='__main__':
    main()