from django.db import models

class BlogPost(models.Model):
    name = models.CharField(max_length=100)
    issueID = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='blog/thumbnails/')
    video = models.URLField(blank=True)
    image1 = models.ImageField(upload_to='blog/images2/', blank=True)
    image2 = models.ImageField(upload_to='blog/images2/', blank=True)
    image3 = models.ImageField(upload_to='blog/images2/', blank=True)
    image4 = models.ImageField(upload_to='blog/images2/', blank=True)
    image5 = models.ImageField(upload_to='blog/images2/', blank=True)
    category = models.CharField(max_length=50 , default="mobile")
    client = models.CharField(max_length=100 , default="user" , blank=True)
    project_issue = models.DateField()
    project_finish = models.DateField()
    repairing_cost = models.DecimalField(max_digits=10, decimal_places=2 , default="hidden")
    description = models.TextField()

    def __str__(self):
        return self.name

