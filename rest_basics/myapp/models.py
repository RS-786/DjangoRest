from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    hobby = models.CharField(max_length=64)

    def __str__(self):
        return self.name