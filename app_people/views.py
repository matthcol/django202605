from django.shortcuts import render

# Recap des ViewSet et Mixins
from rest_framework.viewsets import (
    ViewSet,
    GenericViewSet,
    ReadOnlyModelViewSet, # list + retrieve
    ModelViewSet
)
from rest_framework.mixins import (
    ListModelMixin, 
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin, 
    DestroyModelMixin
)
from rest_framework.response import Response

from app_people.models import Person
from app_people.serialisers import PersonSerializer


# Create your views here.

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    # Endpoints (tous surchargeables)
    # * create : POST /api/persons
    # * list :  GET /api/persons
    # * retrieve : GET /api/persons/12
    # * update : PUT  /api/persons/12
    # * partial_update : PATCH /api/persons/12
    # * destroy : DELETE /api/persons/12

    # Exemple de surcharge:
    def list(self, request, *args, **kwargs):
        data = self.queryset.order_by('-birthdate')
        return Response(
            self.serializer_class(data, many=True).data
        )

# alternative
class PersonViewSetAlt(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

