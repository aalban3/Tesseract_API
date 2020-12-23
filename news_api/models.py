from django.db import models

# Create your models here.
class News(models.Model):
    article     = models.CharField(max_length=200)
    link        = models.URLField(max_length=200)
    date        = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.article