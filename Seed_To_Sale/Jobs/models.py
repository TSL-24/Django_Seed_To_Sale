from django.db import models
from Employees.models import Employee 

class JobType(models.Model):
	job_type_id = models.IntegerField(primary_key=True)
	job_type_name = models.CharField(max_length=100)

	def __str__(self):
		return(self.job_type_name)

class Job(models.Model):
	job_id = models.AutoField(primary_key=True)
	job_is_complete = models.BooleanField()
	job_name = models.CharField(max_length=200)
	job_desc = models.CharField(max_length=500)
	job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
	job_create_date = models.DateTimeField(auto_now_add=True)
	job_start = models.DateTimeField(auto_now_add=False)
	job_end = models.DateTimeField()
	job_lot = models.CharField(max_length=200, blank=True)
	job_batch = models.CharField(max_length=200, blank=True)

	def __str__ (self):
		return(self.job_name)

class TaskType(models.Model):
	task_type_id = models.IntegerField(primary_key=True)
	task_type_parent = models.ForeignKey(JobType, on_delete=models.CASCADE)
	task_type_name = models.CharField(max_length=100)
	task_type_desc = models.CharField(max_length=500, blank=True)

	def __str__(self):
		return(self.task_name)

class Task(models.Model):
	task_id = models.AutoField(primary_key=True)
	task_is_complete = models.BooleanField()
	task_name = models.CharField(max_length=100)
	task_desc = models.CharField(max_length=500)
	task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
	task_job = models.ForeignKey(Job, on_delete=models.CASCADE)

	def __str__(self):
		return(self.task_name)

class TaskLog(models.Model):
	task_log_id = models.AutoField(primary_key=True)
	task_log_job = models.ForeignKey(Job, on_delete=models.CASCADE)
	task_log_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
	task_log_tstamp = models.DateTimeField(auto_now_add=True)
	task_log_data = models.JSONField()

	