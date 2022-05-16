from django.db import models

class Information(models.Model):
    organization = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    location = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name = "College Information"
        verbose_name_plural = "College Information"
    
    def __str__(self):
        return self.organization
    