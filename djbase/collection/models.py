# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Artist(models.Model):
	name = models.CharField(unique=True, max_length=255)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.name


class Album(models.Model):
	name = models.CharField(max_length=255)
	artists = models.ManyToManyField(Artist)

	def __unicode__(self):
		return self.name


class Genre(models.Model):
	name = models.CharField(unique=True, max_length=255)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.name


class SongTags(models.Model):
	name = models.CharField(max_length=100)
	slug = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name


class Song(models.Model):
	name = models.CharField(max_length=255)
	artists = models.ManyToManyField(Artist)
	genres = models.ManyToManyField(Genre, blank=True)
	bpm = models.PositiveIntegerField(null=True, blank=True)
	tags = models.ManyToManyField(SongTags, blank=True)
	albums = models.ManyToManyField(Album, blank=True)

	def __unicode__(self):
		return self.name


class CUEPoint(models.Model):
	song = models.ForeignKey(Song)
	point = models.CharField(max_length=6)
	annotation = models.CharField(max_length=255, blank=True)
