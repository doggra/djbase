# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Artist, Genre, Song
from .serializers import ArtistSerializer, GenreSerializer, SongSerializer
from rest_framework import generics


##### Views

class SongListView(ListView):
	model = Song

##### APIs

class ArtistAPI(generics.ListCreateAPIView):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer


class GenreAPI(generics.ListCreateAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer


class SongAPI(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
