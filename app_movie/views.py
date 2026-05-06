from typing import override

from django.shortcuts import render
from django.db.models import QuerySet

from rest_framework.viewsets import ModelViewSet

from app_movie.models import Movie
from app_movie.serializers import (
    MovieSimpleSerializer,
    MovieDetailSerializer,
    MovieSaveSerializer
)

# Create your views here.

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()  # requis par le router pour le basename

    @override
    def get_queryset(self) -> QuerySet[Movie]:
        match self.action:
            case 'list':
                return Movie.objects.only('id', 'title', 'year') 
            case _:
                return Movie.objects.select_related('director') \
                    .prefetch_related('actors')

    @override
    def get_serializer_class(self):
        # https://peps.python.org/pep-0636/
        match self.action:
            case 'retrieve':
                return MovieDetailSerializer
            case 'list':
                return MovieSimpleSerializer
            case _:
                return MovieSaveSerializer

