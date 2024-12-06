from django.db import models
from Employees.models import Employee 

class JobType(models.Model):
	type_id = models.IntegerField(primary_key=True)
	type_name = models.CharField(max_length=100)

	def __str__(self):
		return(self.type_name)

class Job(models.Model):
	job_id = models.AutoField(primary_key=True)
	job_is_complete = models.BooleanField()
	job_name = models.CharField(max_length=200)
	job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
	job_create_date = models.DateTimeField(auto_now_add=True)
	job_start = models.DateTimeField(auto_now_add=False)
	job_end = models.DateTimeField()
	job_lot = models.CharField(max_length=200, blank=True)
	job_batch = models.CharField(max_length=200, blank=True)

	def __str__ (self):
		return(self.job_name)

class TaskLog(models.Model):
	task_id = models.AutoField(primary_key=True)
	task_job = models.ForeignKey(Job, on_delete=models.CASCADE)
	employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
	task_tstamp = models.DateTimeField(auto_now_add=True)
	task_data = models.JSONField()
