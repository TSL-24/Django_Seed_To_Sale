from django.contrib import admin

from .models import Job, JobType, TaskLog, TaskType, Task

admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(TaskLog)
admin.site.register(TaskType)
admin.site.register(Task)