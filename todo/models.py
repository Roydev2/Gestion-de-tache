from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=120)
    responsable = models.CharField(max_length=120)
    start = models.DateField(default=timezone.now)
    end = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
