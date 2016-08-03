from django.db import models
 
class posts(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    
# Create your models here.
