from django.contrib import admin
from .models import Department, Professor


# @admin.register(Department)
# class Department_admin(admin.ModelAdmin):
#     pass


# @admin.register(Professor)
# class Professor_admin(admin.ModelAdmin):
#     pass

admin.site.register([Department, Professor])
