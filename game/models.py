from __future__ import unicode_literals

from django.db import models

class Card(models.Model):
	word = models.CharField(max_length = 50)
	color = models.CharField(max_length = 10)
	visibility = models.BooleanField()

