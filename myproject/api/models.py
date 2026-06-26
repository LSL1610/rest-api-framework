from django.db import models

# Create your models here.
class Domain(models.Model):
    slug = models.CharField(max_length=100)
    domain = models.JSONField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.slug