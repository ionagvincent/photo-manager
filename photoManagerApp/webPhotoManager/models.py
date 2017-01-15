from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    username = models.CharField(blank=False, unique=True, max_length=50)

class Provider(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=50)
    path_convention = models.CharField(max_length=255)
    bucket_name = models.CharField(max_length=100)

class Photo(models.Model):
    file_name = models.CharField(blank=False, unique=True, max_length=80)
    width = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    checksum = models.CharField(blank=False, unique=True, max_length=32)
    owner = models.ForeignKey(User, blank=False)
    file_size = models.IntegerField(blank=False)
    upload_date = models.DateField(blank=False)
    date_taken = models.DateField(blank=False)
    providers = models.ForeignKey(Provider)

class Album(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=100)