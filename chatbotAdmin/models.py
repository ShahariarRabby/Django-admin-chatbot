# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Fb_users(models.Model):
    fb_id = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    locale = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    timezone = models.IntegerField()




class houz_admin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

