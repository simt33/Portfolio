from django.db import models


class TechEntry(models.Model):
    title = models.CharField(max_length=200)
    tech_used = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def summary(self):
        maxlength = 150
        if len(self.body) > maxlength:
            return self.body[:maxlength] + "..."
        else:
            return self.body

    def __str__(self):
        return self.title
