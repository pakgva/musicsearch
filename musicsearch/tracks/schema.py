import graphene

from graphene_django.types import DjangoObjectType

from musicsearch.tracks.models import Artist, Album, Track

class ArtistType(DjangoObjectType):
  class Meta:
    model = Artist

class AlbumType(DjangoObjectType):
  class Meta:
    model = Album

class TrackType(DjangoObjectType):
  class Meta:
    model = Track

  artists = graphene.List(ArtistType)

  def resolve_artists(self, args, context, info):
    return self.artists.all()

class Query(graphene.AbstractType):
  query_artists = graphene.Field(ArtistType,
                                 id=graphene.Int(),
                                 byName=graphene.String())

  def resolve_query_artists(self, args, context, info):
    id = args.get('id')
    name = args.get('byName')

    if id is not None:
      return Artist.objects.get(pk=id)

    if name is not None:
      return Artist.objects.get(name=name)

    return None
