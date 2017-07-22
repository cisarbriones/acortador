from django.db import models
# Create your models here.
class Acortar(models.Model):
	url = models.CharField(max_length=220,)
	code = models.CharField(max_length=15, unique=True)


	def __str__(self):
		return (self.url)