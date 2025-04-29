from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextField

from projects.models import Project

User = get_user_model()

class Status(models.Model):
    code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        return self.name


class Label(models.Model):
    code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    labels = models.ManyToManyField(Label, blank=True, related_name='tasks')
    assignees = models.ManyToManyField(User, blank=True, related_name='assignees_tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks') # кем создана задача
    started_at = models.DateField(auto_now_add=True) # дата начала
    due_date = models.DateField(null=True, blank=True) # дата окончания

    def __str__(self):
        return self.title

class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)