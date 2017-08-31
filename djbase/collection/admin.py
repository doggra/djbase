# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Artist, Genre, Song


admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Song)
