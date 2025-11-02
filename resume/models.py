from django.db import models

class Resume(models.Model):
    title = models.CharField(max_length=255, default="Untitled Resume")
    created_at = models.DateTimeField(auto_now_add=True)


class PersonalDetail(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255, blank=True)
    school = models.CharField(max_length=255, blank=True)
    years = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    years = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
