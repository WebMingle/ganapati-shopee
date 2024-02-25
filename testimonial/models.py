from django.db import models

def get_default_image():
    return '../static/avatar.jpg'

class Post(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial_images/', default=get_default_image, blank=True, null=True)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.name
