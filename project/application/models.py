from django.db import models

class Storage(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(max_length=30)