from django.db import models

class Message(models.Model):
	title = models.Charfield(max_length=50)
	body = models.Charfield(max_length=150)