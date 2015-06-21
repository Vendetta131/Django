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
    photo = models.ImageField(upload_to='.')

    def __unicode__(self):
        return self.title


