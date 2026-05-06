from django.db import models

from app_people.models import Person

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.PositiveIntegerField()
    duration = models.PositiveSmallIntegerField(null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)

    # associations

    # director : manytoone
    director = models.ForeignKey(
        Person, 
        related_name='directed_movies', 
        null=True, 
        blank=True,
        on_delete=models.SET_NULL, 
    )
    
    # actors : manytomany
    actors = models.ManyToManyField(
        Person, 
        related_name='played_movies', 
        through='Play', 
        through_fields=('movie', 'actor')
    )


class Play(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='plays')
    actor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='plays')

    # association field(s)  
    character = models.CharField(max_length=100)