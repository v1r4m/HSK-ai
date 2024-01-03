from django.db import models

class Prompt(models.Model):
    prompt = models.TextField()
    grade = models.CharField(max_length=200)
    type = models.IntegerField()
    index = models.IntegerField()