from django.db import models


class Resume(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PersonalDetail(models.Model):
    resume = models.OneToOneField(
        Resume, on_delete=models.CASCADE, related_name="personal", null=True, blank=True
    )
    full_name = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=60, blank=True)
    location = models.CharField(max_length=120, blank=True)
    website = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)
    about = models.TextField(blank=True)


class Language(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="languages"
    )
    name = models.CharField(max_length=80)
    level = models.IntegerField(default=3)


class Certificate(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="certificates"
    )
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=300, blank=True)
    link = models.CharField(max_length=300, blank=True)


class Education(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="educations"
    )
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20, blank=True)
    end_date = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)


class Experience(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="experiences"
    )
    title = models.CharField(max_length=200)
    employer = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20, blank=True)
    end_date = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)


class Project(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="projects"
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=20, blank=True)
    end_date = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)
