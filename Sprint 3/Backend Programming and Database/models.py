from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField


# USER FEEDBACK MODEL USED FOR "CONTACT ME" WEBPAGE
class Feedback(models.Model):
	name = models.CharField(max_length=100)
	concern = models.CharField(max_length=100)
	message = TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name}-{self.email}"

class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
 
    def __str__(self):
    	return f"{self.firstname} {self.lastname}"

class ShareMessage(models.Model):
	sName = models.CharField(max_length=100)
	sMessage = TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.sName}-{self.sMessage}"