from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    PrimaryKeyRelatedField,
    Serializer,
)

from app_movie.models import Movie, Play
from app_people.models import Person
from app_people.serialisers import PersonSerializer

class MovieSaveSerializer(ModelSerializer):
    # director = PrimaryKeyRelatedField(queryset=Person.objects.all()) # auto

    class Meta:
        model = Movie
        exclude = ['actors']

class PlayDetailSerializer(ModelSerializer):
    actor = PersonSerializer(read_only=True)

    class Meta:
        model = Play
        fields = ['actor', 'character']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        actor_data = data.pop('actor')
        return {**actor_data, 'character': data['character']}


class MovieDetailSerializer(ModelSerializer):
    director = PersonSerializer(read_only=True)
    actors   = PlayDetailSerializer(many=True, source='plays', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class MovieSimpleSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = 'id', 'title', 'year',


class PlayInputSerializer(Serializer):
    actor     = PrimaryKeyRelatedField(queryset=Person.objects.all())
    character = CharField(max_length=100)

