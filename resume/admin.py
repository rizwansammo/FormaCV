from django.contrib import admin
from .models import Resume, PersonalDetail, Education, Experience, Project

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")

@admin.register(PersonalDetail)
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "resume")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "resume")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "resume")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "resume")
