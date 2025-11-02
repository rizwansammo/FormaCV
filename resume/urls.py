from django.urls import path
from . import views

urlpatterns = [
    path("", views.builder, name="builder"),
    path("save-personal/", views.save_personal, name="save_personal"),
    path("add-education/", views.add_education, name="add_education"),
    path("add-experience/", views.add_experience, name="add_experience"),
    path("add-project/", views.add_project, name="add_project"),
    path("add-certificate/", views.add_certificate, name="add_certificate"),
    path("add-language/", views.add_language, name="add_language"),
    path("preview/", views.preview_template, name="preview"),
    path("export-pdf/", views.export_pdf, name="export_pdf"),
]
