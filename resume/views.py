from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now

from .models import Resume, PersonalDetail, Education, Experience, Project
from .forms import PersonalDetailForm

def _get_resume(request):
    rid = request.session.get("resume_id")
    resume = None
    if rid:
        try:
            resume = Resume.objects.get(id=rid)
        except Resume.DoesNotExist:
            resume = None
    if not resume:
        resume = Resume.objects.create(title="My Resume", created_at=now())
        request.session["resume_id"] = resume.id
    return resume

def builder(request):
    resume = _get_resume(request)
    personal = PersonalDetail.objects.filter(resume=resume).first()
    education = Education.objects.filter(resume=resume).order_by("id").first()
    experience = Experience.objects.filter(resume=resume).order_by("id").first()
    project = Project.objects.filter(resume=resume).order_by("id").first()

    ctx = {
        "personal": personal,
        "education": education,
        "experience": experience,
        "project": project,
    }
    return render(request, "builder.html", ctx)

@require_POST
def api_save_personal(request):
    resume = _get_resume(request)
    instance = PersonalDetail.objects.filter(resume=resume).first()
    form = PersonalDetailForm(request.POST, request.FILES, instance=instance)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.resume = resume
        obj.save()
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)

@require_POST
def api_save_education(request):
    resume = _get_resume(request)
    obj, _ = Education.objects.get_or_create(resume=resume)
    obj.degree = request.POST.get("degree", "")
    obj.school = request.POST.get("school", "")
    obj.description = request.POST.get("desc", "")
    obj.location = ""
    obj.start_date = None
    obj.end_date = None
    obj.link = ""
    obj.save()
    return JsonResponse({"ok": True})

@require_POST
def api_save_experience(request):
    resume = _get_resume(request)
    obj, _ = Experience.objects.get_or_create(resume=resume)
    obj.title = request.POST.get("title", "")
    obj.employer = request.POST.get("company", "")
    obj.description = request.POST.get("desc", "")
    obj.location = ""
    obj.start_date = None
    obj.end_date = None
    obj.link = ""
    obj.save()
    return JsonResponse({"ok": True})

@require_POST
def api_save_project(request):
    resume = _get_resume(request)
    obj, _ = Project.objects.get_or_create(resume=resume)
    obj.title = request.POST.get("title", "")
    obj.subtitle = request.POST.get("subtitle", "")
    obj.description = request.POST.get("desc", "")
    obj.link = ""
    obj.start_date = None
    obj.end_date = None
    obj.save()
    return JsonResponse({"ok": True})
