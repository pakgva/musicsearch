import graphene

import musicsearch.tracks.schema

class Query(musicsearch.tracks.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
