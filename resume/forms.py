from django import forms
from .models import PersonalDetail, Education, Experience, Project

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
        fields = ["degree", "school", "years", "description"]

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "company", "years", "description"]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "subtitle", "description"]
