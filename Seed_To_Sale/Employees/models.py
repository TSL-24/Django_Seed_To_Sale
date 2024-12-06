from django.db import models

# Create your models here.
class Employee(models.Model):

	emp_id = models.IntegerField(primary_key=True)
	emp_is_active = models.BooleanField()
	emp_is_manager = models.BooleanField(default=False)
	emp_first_name = models.CharField(max_length=50)
	emp_last_name = models.CharField(max_length=50)
	emp_dob = models.DateField()
	emp_start_date = models.DateField()
	
	def __str__(self):
		return f'{self.emp_first_name} {self.emp_last_name}'