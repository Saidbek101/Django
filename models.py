from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255, unique=True, default='a', null=True)
    pub_date = models.DateTimeField('Date published', null=True)