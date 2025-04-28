from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextField

from projectflow.projects.models import Project

User = get_user_model()

class Status(models.Model):
    name = models.CharField(max_length=50)


class Label(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    labels = models.ManyToManyField(Label, blank=True, related_name='tasks')
    assignees = models.ManyToManyField(User, blank=True, related_name='assignees_tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    started_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)