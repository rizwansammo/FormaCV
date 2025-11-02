from django.contrib import admin
from .models import (
    Resume,
    PersonalDetail,
    Education,
    Experience,
    Project,
    Certificate,
    Language,
)

admin.site.register(Resume)
admin.site.register(PersonalDetail)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(Language)
