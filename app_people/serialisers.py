from datetime import date

from rest_framework.serializers import (
    Serializer,
    ListSerializer, # interne
    SerializerMethodField, # interne
    HyperlinkedModelSerializer,
    ModelSerializer,
)

from app_people.models import Person

class PersonSerializer(ModelSerializer):
    age = SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    def get_age(self, obj):
        if obj.birthdate is None:
            return None
        today = date.today()
        delta_year = today.year - obj.birthdate.year
        if (today.month, today.day) >= (obj.birthdate.month, obj.birthdate.day):
            return delta_year
        else:
            return delta_year - 1