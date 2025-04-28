from django.contrib import admin
from .models import Status, Label, Task, TaskComment

admin.site.register(Status)
admin.site.register(Label)
admin.site.register(Task)
admin.site.register(TaskComment)
