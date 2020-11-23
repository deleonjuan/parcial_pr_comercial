import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from pelicula.models import Pelicula


class PeliculaNode(DjangoObjectType):
    class Meta:
        model = Pelicula
        filter_fields = {
            'titulo': ['exact', 'icontains', 'istartswith'],
            'descripcion': ['exact', 'icontains'],
            'estreno': ['exact', 'icontains'],
            'portada': ['exact', 'icontains'],
            'genero': ['exact'],
            # 'genero__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):

    pelicula = relay.Node.Field(PeliculaNode)
    all_peliculas = DjangoFilterConnectionField(PeliculaNode)