from datetime import date

from django.db import models

# Create your models here.

class Person(models.Model):
    # PK : id auto ou AutoField
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    is_alive = models.BooleanField(default=True)
    
    # age = models.PositiveSmallIntegerField()

    
    
