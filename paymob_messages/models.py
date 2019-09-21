from django.db import models

class Message(models.Model):
	title = models.CharField(max_length=50)
	body = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published', auto_now=True)

	def __str__(self):
		return self.title + ' : ' + self.body + ' (' + self.pub_date.strftime("%d/%m/%Y %H:%M:%S") + ')'