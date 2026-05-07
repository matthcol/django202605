from typing import cast, override

from django.shortcuts import render
from django.db.models import QuerySet

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app_movie.models import Movie, Play
from app_movie.serializers import (
    MovieSimpleSerializer,
    MovieDetailSerializer,
    MovieSaveSerializer,
    PlayInputSerializer,
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
            case _: # create, update, partial_update, destroy
                return MovieSaveSerializer


    def _detail_response(self, pk, http_status=status.HTTP_200_OK):
        instance = Movie.objects.select_related('director').prefetch_related('actors').get(pk=pk)
        return Response(MovieDetailSerializer(instance).data, status=http_status)

    @override
    def create(self, request, *_args, **_kwargs):
        serializer = MovieSaveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = cast(Movie, serializer.save())
        return self._detail_response(movie.pk, status.HTTP_201_CREATED)

    # TODO : merge update et partial_update
    @override
    def update(self, request, *_args, **_kwargs):
        partial = _kwargs.get('partial', False)
        instance = self.get_object()
        serializer = MovieSaveSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return self._detail_response(instance.pk)

    # NB: partial_updare hanfled by update

    # @override
    # def partial_update(self, request, *_args, **_kwargs):
    #     instance = self.get_object()
    #     serializer = MovieSaveSerializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return self._detail_response(instance.pk)
    
    @action(detail=True, methods=['put'], url_path='casting')
    def casting(self, request, *_args, **_kwargs):
        movie = self.get_object()
        serializer = PlayInputSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        Play.objects.filter(movie=movie).delete()
        Play.objects.bulk_create([
            Play(movie=movie, actor=item['actor'], character=item['character'])
            for item in serializer.validated_data
        ])
        return self._detail_response(movie.pk)