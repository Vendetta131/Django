# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


    #class Description(models.Model):
    #first = models.CharField(max_length=30)
    #last = models.CharField(max_length=30)

    #def __unicode__(self):            
        #return (self.first, self.last)

class Building(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    glav = models.ImageField(upload_to='.')

    def __unicode__(self):
        return self.title

class Photo(models.Model):
    name = models.CharField(max_length=30,blank=True)
    one = models.ImageField(upload_to='./Other',blank=True)
    second = models.ImageField(upload_to='./Other', blank=True)
    third = models.ImageField(upload_to='./Other', blank=True)
    fourth = models.ImageField(upload_to='./Other', blank=True)
    fifth = models.ImageField(upload_to='./Other', blank=True)
    sixth = models.ImageField(upload_to='./Other', blank=True)
    sborka = models.ForeignKey(Building,null=True)

    def __unicode__(self):
        return self.name



