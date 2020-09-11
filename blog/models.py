from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=True)
    body = models.CharField(max_length=4000)
    image = models.ImageField(upload_to='images')
