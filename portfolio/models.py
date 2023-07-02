from django.db import models

# Create your models here.


class enquiry(models.Model):
	ip = models.CharField(max_length=255,null=True,blank=True)
	name = models.CharField(max_length=255,null=False,blank=False)
	email = models.CharField(max_length=255,null=True,blank=True)
	mobile = models.CharField(max_length=255,null=True,blank=True)
	subject = models.CharField(max_length=255,null=False,blank=False)
	message = models.TextField(max_length=255,null=False,blank=False)
	status= models.CharField(max_length=255,default='Incomplete')
	def __str__(self):
		return self.name