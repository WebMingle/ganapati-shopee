from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    website_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='member_images/', blank=True, null=True)

    def __str__(self):
        return self.name

