from django import forms
from .models import (
    PersonalDetail,
    Education,
    Experience,
    Project,
    Certificate,
    Language,
)


class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        fields = [
            "full_name",
            "title",
            "email",
            "phone",
            "location",
            "website",
            "linkedin",
            "photo",
            "about",
        ]


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            "degree",
            "school",
            "start_date",
            "end_date",
            "location",
            "description",
            "link",
        ]


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "employer",
            "start_date",
            "end_date",
            "location",
            "description",
            "link",
        ]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "subtitle", "start_date", "end_date", "description", "link"]


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ["title", "details", "link"]


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ["name", "level"]
