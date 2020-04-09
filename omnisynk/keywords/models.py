from django.db import models
from django.utils import  timezone

# Create your models here.
class Example(models.Model):
    text = models.CharField(max_length=4000)
    created = models.DateTimeField(default = timezone.now())

class KeyWordsGenerationMethods(models.Model):
    name = models.CharField(max_length=100)

class KeyWordsGenerationResults(models.Model):
    created = models.DateTimeField(default=timezone.now())
    id_example = models.ForeignKey(Example, on_delete=models.DO_NOTHING, default=0)
    method_name = models.CharField(max_length=100, default='null')
    keywords = models.CharField(max_length=4000, default='null')


