import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import (
    Resume,
    PersonalDetail,
    Education,
    Experience,
    Project,
    Certificate,
    Language,
)
from .forms import (
    PersonalDetailForm,
    EducationForm,
    ExperienceForm,
    ProjectForm,
    CertificateForm,
    LanguageForm,
)
from django.template.loader import render_to_string
from weasyprint import HTML


def get_or_create_resume(request):
    rid = request.session.get("resume_id")
    if rid:
        try:
            return Resume.objects.get(id=rid)
        except Resume.DoesNotExist:
            pass
    r = Resume.objects.create()
    PersonalDetail.objects.create(resume=r)
    request.session["resume_id"] = r.id
    return r


def builder(request):
    resume = get_or_create_resume(request)
    context = {
        "resume": resume,
        "personal_form": PersonalDetailForm(instance=resume.personal),
        "education_form": EducationForm(),
        "experience_form": ExperienceForm(),
        "project_form": ProjectForm(),
        "certificate_form": CertificateForm(),
        "language_form": LanguageForm(),
        "educations": resume.educations.all(),
        "experiences": resume.experiences.all(),
        "projects": resume.projects.all(),
        "certificates": resume.certificates.all(),
        "languages": resume.languages.all(),
    }
    return render(request, "builder.html", context)


@require_POST
def save_personal(request):
    resume = get_or_create_resume(request)
    form = PersonalDetailForm(request.POST, request.FILES, instance=resume.personal)
    if form.is_valid():
        form.save()
        return redirect("builder")
    return redirect("builder")


@require_POST
def add_education(request):
    resume = get_or_create_resume(request)
    form = EducationForm(request.POST)
    if form.is_valid():
        e = form.save(commit=False)
        e.resume = resume
        e.save()
    return redirect("builder")


@require_POST
def add_experience(request):
    resume = get_or_create_resume(request)
    form = ExperienceForm(request.POST)
    if form.is_valid():
        e = form.save(commit=False)
        e.resume = resume
        e.save()
    return redirect("builder")


@require_POST
def add_project(request):
    resume = get_or_create_resume(request)
    form = ProjectForm(request.POST)
    if form.is_valid():
        p = form.save(commit=False)
        p.resume = resume
        p.save()
    return redirect("builder")


@require_POST
def add_certificate(request):
    resume = get_or_create_resume(request)
    form = CertificateForm(request.POST)
    if form.is_valid():
        c = form.save(commit=False)
        c.resume = resume
        c.save()
    return redirect("builder")


@require_POST
def add_language(request):
    resume = get_or_create_resume(request)
    form = LanguageForm(request.POST)
    if form.is_valid():
        l = form.save(commit=False)
        l.resume = resume
        l.save()
    return redirect("builder")


def preview_template(request):
    resume = get_or_create_resume(request)
    return render(request, "resume_preview.html", {"resume": resume})


def export_pdf(request):
    resume = get_or_create_resume(request)
    html = render_to_string("resume_preview.html", {"resume": resume})
    pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="FormaCV.pdf"'
    return response
