# coding: utf-8
from django.db import models

# Create your models here.
class MeetingRoom(models.Model):
    AVAILABLE = 0
    OCCUPIED = 1
    STATUS_CHOICE = (
        (AVAILABLE, 'Available'),
        (OCCUPIED, 'Occupied'),
        )
    name = models.CharField(max_length=128)
    # status = models.IntegerField(choices=STATUS_CHOICE, default=AVAILABLE)
    #floor = models.CharField(max_length=128)
    #capacity = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=64)
    phone = models.IntegerField(max_length=11, unique=True)
    dept = models.CharField(max_length=128)
    def __unicode__(self):
        return '%s, %s' % (self.name, self.phone)

class Reservation(models.Model):
    AM = 0
    PM = 1
    TIME_CHOICE = (
        (AM, 'AM'),
        (PM, 'PM'),
        )
    DENY_STATUS = 0
    PENDING_STATUS = 1
    AGREE_STATUS = 2
    STATUS_CHOICE = (
        (AGREE_STATUS, 'Agree'),
        (DENY_STATUS, 'Deny'),
        (PENDING_STATUS, 'Pending'),
        )
    contact = models.ForeignKey(Contact)
    room = models.ForeignKey(MeetingRoom)
    book_date = models.DateField()
    book_time = models.IntegerField(choices=TIME_CHOICE, default=AM)
    subscribe_time = models.DateTimeField(auto_now_add=True)
    vip = models.CharField(max_length=256)
    count = models.IntegerField(max_length=3)
    status = models.IntegerField(choices=STATUS_CHOICE)
    def __unicode__(self):
        return '%s, %s' % (self.contact.name, self.room.name)