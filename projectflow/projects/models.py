import secrets

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True) # пустое поле будет сохранено как пустая строка
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="owned_projects")
    members = models.ManyToManyField(User, through="ProjectMember", related_name="projects")
    invite_token = models.CharField(max_length=255, unique=True, default=secrets.token_urlsafe)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("member", "Member"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="member")
