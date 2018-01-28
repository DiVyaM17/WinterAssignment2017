# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Comment to self: Change User to settings.AUTH_USER_MODEL (django.contrib.auth) 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user_profile')
    follow = models.ManyToManyField(User, related_name = 'user_follow')
    dob = models.DateField(null=True)
    mobile_no = models.IntegerField(null=True)
    interests = models.CharField(max_length = 200,null=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 1000)
    pub_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 200)

    def __str__(self):
        return self.comment
