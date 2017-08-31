from django.conf.urls import url, include
from django.contrib import admin

from .views import SongListView, ArtistAPI, GenreAPI, SongAPI


urlpatterns = [

	# Views
    url(r'^songs/$', SongListView.as_view(), name='song_list'),

    # APIs
    url(r'^songs/api/$', SongAPI.as_view(), name='song_api'),
    url(r'^genres/api/$', GenreAPI.as_view(), name='genre_api'),
    url(r'^artists/api/$', ArtistAPI.as_view(), name='artist_api'),
]
