from django.db import models

# Create your models here.
class Article(models.Model):
    source = models.CharField(max_length=100, blank=True,null=True)
    author = models.CharField(max_length=100, blank=True,null=True)
    title = models.CharField(max_length=1000, blank=True,null=True)
    description = models.TextField( blank=True,null=True)
    url = models.CharField(max_length=2500, blank=True,null=True)
    image_url = models.CharField(max_length=2500, blank=True,null=True)
    content = models.TextField( blank=True,null=True)
    created_at = models.CharField(max_length=100, blank=True,null=True)
    
    def __str__(self) -> str:
        return self.title