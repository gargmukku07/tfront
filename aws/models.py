from __future__ import unicode_literals

from django.db import models

# Create your models here.

class userDetails(models.Model):
	firstname_text = models.CharField(max_length=100)
	lastname_text = models.CharField(max_length=100)


