#models for the 'shopping' django app

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Store(models.Model):
    storeID = models.AutoField(primary_key=True, unique=True)   #unique primary key for the Store class/table
    storeName = models.CharField(max_length=200)    #name of the store
    storeLocation = models.CharField(max_length=200)    #general location of the store (required)
    storeStreet = models.CharField(max_length=200, null=True, blank=True)    #specific street address (optional)
    storeCity = models.CharField(max_length=200, null=True, blank=True)    #specific city (optional)
    storeState = models.CharField(max_length=200, null=True, blank=True)    #specific state (optional)
    storeZip = models.CharField(max_length=11, null=True, blank=True)    #specific zip code (optional)
    #set the foreign key for which items are at the store
    #storeItems = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        store_rep = str(self.storeName) + " - " + str(self.storeLocation)
        return store_rep


class Item(models.Model):
    itemID = models.AutoField(primary_key=True, unique=True)    #unique primary key for the Item class/table
    itemName = models.CharField(max_length=200)    #shorter item name for the product
    itemDescription = models.CharField(max_length=400)    #longer description of the item, if needed
    itemQuantity = models.CharField(max_length=200)    #quantity needed of the item
    itemAdded = models.DateTimeField('Date Added')    #date the item was added

    #item added by
    #itemOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    #will need to add this another way since i'm no longer tracking the user model within the shopping app

    itemStore = models.ForeignKey(Store, on_delete=models.CASCADE)    #store location
    itemPurchased = models.BooleanField()    #this item purchased - not currently being used

    def __str__(self):
        item_rep = str(self.itemName) + ", " + str(self.itemAdded)
        return item_rep