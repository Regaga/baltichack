# -*- coding:utf-8 -*-
from django.utils import timezone
from django.conf import settings
from django.db import models
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length = 32)
    image = models.ImageField(upload_to = './', null = True)
    
    def __str__(self):
        return self.title


class City(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    
       def __str__(self):
           return self.post


class Poll(models.Model):
    question = models.CharField(max_length=200)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Votes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)


    @classmethod
    def create(cls, user, choice):
        vote = cls(user=user, choice=choice)
        return vote
