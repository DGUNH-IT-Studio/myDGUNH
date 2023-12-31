from django.db import models
from datetime import datetime


DEFAULT_PROFESSOR_SCHEDULE = [
    {
        "Monday": [],
        "Tuesday": [],
        "Wednsday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": []
    },
    {
        "Monday": [],
        "Tuesday": [],
        "Wednsday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": []
    }
]


class term(models.Model):
    term_num = models.IntegerField()
    term_start = models.DateField(blank=True)
    term_end = models.DateField(blank=True)

    objects = models.Manager()  # default using manager


    def __str__(self):
        return str(self.term_num) + '-й семестр (' + \
               str(self.term_start) + ' - ' + \
               str(self.term_end) + ')'


    class Meta:
        unique_together = ('term_num', 'term_start', 'term_end')


class university_faculty(models.Model):
    faculty_full_name = models.CharField(max_length=128, blank=False)
    faculty_short_name = models.CharField(max_length=32, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.faculty_full_name


    class Meta:
        unique_together = ['faculty_full_name', 'faculty_short_name']


class education_profile(models.Model):
    faculty = models.ForeignKey(university_faculty, on_delete=models.CASCADE)
    profile = models.CharField(max_length=256)

    objects = models.Manager()


    def __str__(self):
        return self.profile


    class Meta:
        unique_together = ['faculty', 'profile']


class education_program(models.Model):
    class education_level_choices(models.TextChoices):
        COLLEGE = 'К', 'Колледж'
        BACHELOR = 'Б', 'Бакалавр'
        SPECIALITY = 'С', 'Специалитет'
        MASTER = 'М', 'Магистратура'


    class education_form_choices(models.TextChoices):
        FULLTIME = 'О', 'Очная форма'
        CORRESPONDENSE = 'З', 'Заочная форма'
        PARTTIME = 'ОЗ', 'Очно-заочная форма'
        ONLINE = 'ДИСТ', 'Дистанционная форма'


    profile = models.ForeignKey(education_profile, on_delete=models.CASCADE)
    education_level = models.CharField(
        max_length=1,
        choices=education_level_choices.choices,
    )
    education_form = models.CharField(
        max_length=4,
        choices=education_form_choices.choices,
        default=education_form_choices.FULLTIME,
    )
    education_program_name = models.CharField(
        max_length=256,
        blank=True,
        null=True
    )

    objects = models.Manager()


    def __str__(self):
        return self.education_program_name


    class Meta:
        # ordering = ['Faculty', 'EducationLevel', 'EducationForm', 'EduProgram']
        pass


class university_group(models.Model):
    group_education_program = models.ForeignKey(
        education_program,
        on_delete=models.CASCADE
    )
    course = models.IntegerField(default=1)
    stream = models.IntegerField(default=1)
    group_num = models.IntegerField(default=1)
    subgroup_num = models.IntegerField(blank=True, null=True)

    objects = models.Manager()


    def __str__(self):
        return str(self.group_education_program) + ' ' + str(self.course) + '-' + str(self.group_num)

    class Meta:
        # ordering = ['EduProgram', 'Course', 'Stream', 'GroupNum']
        pass


class student_schedule(models.Model):
    group = models.ForeignKey(
        university_group,
        on_delete=models.CASCADE
    )
    term_num = models.ForeignKey(
        term,
        on_delete=models.CASCADE,
    )
    date_start = models.DateField(blank=True)
    date_end = models.DateField(blank=True)
    schedule_object = models.JSONField(blank=True)


    objects = models.Manager()


    def __str__(self):
        return str(self.group) + ' schedule'


    class Meta:
        # unique_together = (('term_num', 'date_start'), ('term_num', 'date_end'))
        ordering = ['term_num', 'date_start', 'date_end']


class department(models.Model):
    department_name = models.CharField(max_length=256, unique=True)
    subjects = models.JSONField(blank=True)

    objects = models.Manager()


    def __str__(self):
        return self.department_name


    class Meta:
        pass


class teacher(models.Model):    
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_department = models.ForeignKey(department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    schedule_view_name = models.CharField(
        max_length=64, 
        blank=True, 
        null=True,
    )

    objects = models.Manager()


    def __str__(self):
        return str(self.second_name).capitalize() + ' ' + \
               str(self.first_name)[0].upper() + '.' + \
               str(self.last_name)[0].upper() + '.'


    class Meta:
        unique_together = ['teacher_department', 'first_name', 'second_name', 'last_name']


class teacher_schedule(models.Model):
    teacher_info = models.ForeignKey(teacher, on_delete=models.CASCADE)
    # term_num = models.ForeignKey(
    #     term,
    #     on_delete=models.CASCADE,
    # )
    teacher_schedule = models.JSONField(blank=True)
    date_start = models.DateField(blank=True, null=True, default=datetime.fromisoformat("2023-09-01").date())
    date_end = models.DateField(blank=True, null=True, default=datetime.fromisoformat("2023-12-31").date())

    objects = models.Manager()

    def __str__(self):
        return str(self.teacher_info) + ' schedule'

    class Meta:
        # unique_together = [['term_num', 'date_start'], ['term_num', 'date_end']]
        pass
