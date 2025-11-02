from django.contrib import admin
from django.urls import path
from resume import views as r

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", r.builder, name="builder"),

    path("api/personal/save", r.api_save_personal, name="api_personal_save"),
    path("api/education/save", r.api_save_education, name="api_education_save"),
    path("api/experience/save", r.api_save_experience, name="api_experience_save"),
    path("api/projects/save", r.api_save_project, name="api_projects_save"),
]
