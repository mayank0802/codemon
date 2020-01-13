from django.db import models

# Create your models here.
class student_info(models.Model):
	student_id = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=50)
	student_phone = models.IntegerField()
	student_email = models.CharField(max_length = 50)
	student_password = models.CharField(max_length = 60)
	student_city = models.CharField(max_length = 20)
	student_street = models.CharField(max_length = 20)
	student_issue =  models.CharField(default = 'none', max_length = 60)
	def __str__(self): 
		return self.student_name

