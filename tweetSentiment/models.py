from django.db import models
from django.core.validators import RegexValidator
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# Create your models here.
class Tweet(models.Model):
    body            = models.CharField(max_length= 280)
    user            = models.CharField(max_length= 50)
    tweet_id        = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])  
    sentiment       = models.CharField(max_length= 20)
    score           = models.FloatField()
    creation_date   = models.DateTimeField()
    
    def __str__(self):
        return self.body