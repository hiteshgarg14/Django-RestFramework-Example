from __future__ import unicode_literals

from django.db import models

class MyModel(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=120,blank=False)
	desc = models.TextField()
	
	def __str__(self):
		return self.title
