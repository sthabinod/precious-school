from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Events"
        verbose_name_plural = "Events"