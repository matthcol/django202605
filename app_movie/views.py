from typing import cast, override

from django.shortcuts import render
from django.db.models import QuerySet

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from app_movie.models import Movie, Play
from app_movie.serializers import (
    MovieSimpleSerializer,
    MovieDetailSerializer,
    MovieSaveSerializer,
    CastingItemSerializer
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


    def _detail_response(self, pk, http_status=status.HTTP_200_OK):
        instance = Movie.objects.select_related('director').prefetch_related('actors').get(pk=pk)
        return Response(MovieDetailSerializer(instance).data, status=http_status)

    @override
    def create(self, request, *_args, **_kwargs):
        serializer = MovieSaveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = cast(Movie, serializer.save())
        return self._detail_response(movie.pk, status.HTTP_201_CREATED)

    @override
    def update(self, request, *_args, **_kwargs):
        partial = _kwargs.get('partial', False)
        instance = self.get_object()
        serializer = MovieSaveSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return self._detail_response(instance.pk)

    # @override
    # def partial_update(self, request, *_args, **_kwargs):
    #     instance = self.get_object()
    #     serializer = MovieSaveSerializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return self._detail_response(instance.pk)

    # /api/movies/{pk}/casting
    @action(detail=True, methods=['put'], url_path='casting')
    def update_casting(self, request, *_args, **_kwargs):
        instance = self.get_object()
        serializer = CastingItemSerializer(instance, data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        Play.objects.filter(movie=instance).delete()
        Play.objects.bulk_create([
            Play(movie=instance, actor=item['actor'], character=item['character'])
            for item in serializer.validated_data
        ])
        return self._detail_response(instance.pk)