from __future__ import unicode_literals
from django.db import models

# Create your models here
class SignUp(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __unicode__(self):
		return self.email
