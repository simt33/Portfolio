from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images')

    def summary(self):
        maxlength = 150
        if len(self.body) > maxlength:
            return self.body[:maxlength] + "..."
        else:
            return self.body

    def __str__(self):
        return self.title
