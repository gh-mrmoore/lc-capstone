#models for the 'finances' django app

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Banks(models.Model):
    bankID = models.AutoField(primary_key=True, unique=True)    #unique ID for the account
    bankName = models.CharField(max_length=50, unique=True)    #unique name for the account
    bankLocation = models.CharField(max_length=200)    #the name and general location of the bank

    def __str__(self):
        return self.bankName


class LCat(models.Model):
    lcatID = models.AutoField(primary_key=True, unique=True)    #unique ID for each category
    lcatDesc = models.CharField(max_length=50, unique=True)    #unique general description of the category

    def __str__(self):
        return self.lcatDesc


class Line(models.Model):
    lineID = models.AutoField(primary_key=True, unique=True)    #unique id for each transaction logged
    lineDT = models.DateTimeField('Transaction Date')    #date of the transaction
    lineAmount = models.FloatField()    #amount of the transaction
    lineShort = models.CharField(max_length=50)    #short description of the transaction
    lineLong = models.TextField(null=True, blank=True)    #Extended description of the transaction
    lineCategory = models.ForeignKey(LCat, null=True, on_delete=models.SET_NULL)    #Category for the transaction - for analysis
    lineBank = models.ForeignKey(Banks, blank=True, null=True, on_delete=models.CASCADE)    #Set the account for the transaction
    lineBalance = models.FloatField()    #the account balance as of the date of the given transaction

    def __str__(self):
        return self.lineShort