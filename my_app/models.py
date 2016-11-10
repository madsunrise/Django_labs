from django.db import models
from django.contrib.auth.models import User
import datetime

class Service(models.Model):
	title = models.CharField (max_length = 128)
	text = models.TextField()
	added_at = models.DateTimeField(default = datetime.datetime.now)
	author = models.ForeignKey(User)
	price = models.DecimalField(max_digits=7, decimal_places=2)


class Profile(models.Model):
	user = models.OneToOneField(User)

	
	
	
