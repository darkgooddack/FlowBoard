from django.contrib import admin
from .models import Project
from .models import ProjectMember

admin.site.register(Project)
admin.site.register(ProjectMember)