from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    done = models.BooleanField(default=False)
