# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artist(models.Model):
  name = models.CharField(max_length=100)
  image_url = models.CharField(max_length=150)

  def __str__(self):
    return self.name

class Album(models.Model):
  name = models.CharField(max_length=100)
  image_url = models.CharField(max_length=150)
  artist = models.ForeignKey('Artist', related_name='albums')

  def __str__(self):
    return self.name

class Track(models.Model):
  name = models.CharField(max_length=100)
  preview_url = models.CharField(max_length=150)
  track_number = models.IntegerField()
  album = models.ForeignKey('Album', related_name='tracks')
  artists = models.ManyToManyField('Artist')

  def __str__(self):
    return self.name


