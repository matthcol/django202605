from rest_framework.serializers import (
    CharField,
    PrimaryKeyRelatedField,
    ModelSerializer,
    Serializer,
)

from app_movie.models import Movie
from app_people.models import Person
from app_people.serialisers import PersonSerializer

class MovieSaveSerializer(ModelSerializer):
    # director = PersonSerializer()
    # actors = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        exclude = ['actors']

class MovieDetailSerializer(ModelSerializer):
    director = PersonSerializer(read_only=True)
    actors = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class MovieSimpleSerializer(ModelSerializer):
    
    class Meta:
        model = Movie
        fields = 'id', 'title', 'year',

class CastingItemSerializer(Serializer):
    actor = PrimaryKeyRelatedField(queryset=Person.objects.all())
    character = CharField(max_length=100)