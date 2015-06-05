from django.db import models

# Create your models here.
class EmailSignUp(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	subject = models.CharField(max_length=255)
	message = models.TextField(max_length=1000)

	def __str__(self):
		return self.email 