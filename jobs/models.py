from django.db import models


class JobEntry(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    dates = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def summary(self):
        maxlength = 150
        if len(self.description) > maxlength:
            return self.description[:maxlength] + "..."
        else:
            return self.description

    def __str__(self):
        return self.job_title + " @ " + self.company
