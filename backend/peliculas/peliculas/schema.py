import graphene

import pelicula.schema


class Query(pelicula.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)