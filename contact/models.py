from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.fullname

