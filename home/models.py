from django.db import models
from django.urls import path, include

class Subscription(models.Model):
	sno = models.AutoField(primary_key=True)
	subscriptionemail = models.EmailField(max_length=50)
	timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
    		return self.subscriptionemail

