from django.db import models
import random
import string

def code_generator(size=6, chars=string.ascii_lowercase+string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# Create your models here.
class Acortar(models.Model):
	url = models.CharField(max_length=220)
	code = models.CharField(max_length=15, unique=True, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.code = code_generator()
		super(Acortar, self).save(*args, **kwargs)

	def __str__(self):
		return (self.url)
