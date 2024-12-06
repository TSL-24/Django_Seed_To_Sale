from django.contrib import admin

from .models import Job, JobType, TaskLog

admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(TaskLog)