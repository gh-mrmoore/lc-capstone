#models for the 'kids' django app

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Kids(models.Model):
    kidID = models.AutoField(primary_key=True, unique=True)    #unique primary key for the Kids class/table
    kidName = models.CharField(max_length=50)    #name of the kid

    def __str__(self):
        return self.kidName


class Events(models.Model):
    eventsID = models.AutoField(primary_key=True, unique=True)    #unique key for the Events table
    eventsKidID = models.ForeignKey(Kids, on_delete=models.CASCADE)    #reference back to the Kids class for each kid's day
    eventsDate = models.DateField('Event Date')    #date for the events
    eventsTime = models.TimeField()   #time for the events
    eventsGenNote = models.CharField(max_length=40)    #General note for the event that's being added
    eventsExtendedNote = models.TextField(null=True, blank=True)    #Extended note for the event that's being added, optional

    def __str__(self):
        return self.eventsGenNote