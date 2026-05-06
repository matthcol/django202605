from datetime import date

from django.db import models

# Create your models here.

class Person(models.Model):
    # PK : id auto ou AutoField
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    is_alive = models.BooleanField(default=True)
    
    # age = models.PositiveSmallIntegerField()
    def age(self):
        if self.birthdate is None:
            return None
        today = date.today()
        delta_year = today.year - self.birthdate.year
        if (today.month, today.day) >= (self.birthdate.month, self.birthdate.day):
            return delta_year
        else:
            return delta_year - 1
    
    
