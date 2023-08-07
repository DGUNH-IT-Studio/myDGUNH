from django.db import models


class UniversityFaculty(models.model):
    """
    """
    FacultyName = models.CharField(max_length=64)


class Profile(models.model):
    """
    """

    ProfileName = models.CharField(max_length=128)
    UniversityFacultyId = models.ForeignKey(
        UniversityFaculty, on_delete=models.CASCADE
    )


class UniversityGroup(models.model):
    """
    """

    UniversityGroupId = models.IntegerField(primary_key=True)
    FacultyName = models.ForeignObject(
        UniversityFaculty, on_delete=models.CASCADE
    )
    ProfileName = models.OneToOneField(Profile, on_delete=models.CASCADE) # настроить нормальное отношение
    EducationLevel = models.CharField() # одно из Бакалавра или Магистра
    EducationForm = models.CharField() # одно из Очное или Очно-Заочное или Заочное
    StreamNum = models.IntegerField() # задать дефолтное значение
    CourseNum = models.IntegerField() # нужно задать некоторые ограничения в зависимости от формы обучения
    GroupNum = models.IntegerField() # задать дефолтное значение
    SubGroupNum = models.IntegerField() # задать дефолтное значение
    LabGroupNum = models.IntegerField() # задать дефолтное значение
    PracticeGroupNum = models.IntegerField() # задать дефолтное значение
    Schedule = models.JSONField() # посмотреть на аргументы

class CollegeSpeciality(models.Model):
    """
    """

    CollegeSpecialityName = models.CharField(max_length=128)


class CollegeGroup(models.Model):
    """
    """

    CollegeGroupId = models.IntegerField(primary_key=True)
    CollegeSpeciality = models.ForeignKey(CollegeSpeciality, on_delete=models.CASCADE)
    EducationForm = models.CharField()  # одно из Очное или Очно-Заочное или Заочное
    StreamNum = models.IntegerField()  # задать дефолтное значение
    CourseNum = models.IntegerField()  # нужно задать некоторые ограничения в зависимости от формы обучения
    GroupNum = models.IntegerField()  # задать дефолтное значение
    SubGroupNum = models.IntegerField()  # задать дефолтное значение
    LabGroupNum = models.IntegerField()  # задать дефолтное значение
    PracticeGroupNum = models.IntegerField()  # задать дефолтное значение
    Schedule = models.JSONField()  # посмотреть на аргументы