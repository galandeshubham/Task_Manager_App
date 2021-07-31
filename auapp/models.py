from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
	added_by = models.ForeignKey(User, on_delete = models.CASCADE)
	lo = models.CharField(max_length=20) 
