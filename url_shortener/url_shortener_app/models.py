from django.db import models

# Create your models here.
class LongtoShort(models.Model):
    longurl = models.URLField(max_length=250)
    shorturl = models.CharField(max_length=25,unique=True)
    
