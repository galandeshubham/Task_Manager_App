from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
	Task = models.TextField()
	usr = models.ForeignKey(User, on_delete=models.CASCADE)
	dt = models.DateTimeField(auto_now_add = True)
	
	def __str__(s):
		return s.usr.username
