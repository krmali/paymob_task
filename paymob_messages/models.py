from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
	title = models.CharField(max_length=50)
	body = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published', auto_now=True)
	
	""" 
	In DJANGO Documentation, it is recommended to use a custom User model
	but since the project is not intended to be scaled the given User model is used
	""" 
	author = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title + ' : ' + self.body + ' (' + self.pub_date.strftime("%d/%m/%Y %H:%M:%S") + ')'