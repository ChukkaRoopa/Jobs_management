from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField()

    def __str__(self):
        return self.title