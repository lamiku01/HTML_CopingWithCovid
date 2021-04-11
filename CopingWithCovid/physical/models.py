from django.db import models
from django.contrib.auth.models import User

class GratitudeJournal(models.Model):
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

