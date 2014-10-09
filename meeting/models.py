# coding: utf-8
from django.db import models

# Create your models here.
class MeetingRoom(models.Model):
    name = models.CharField(max_length=128)
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
    AGREE_STATUS = 1
    PENDING_STATUS = 2
    STATUS_CHOICE = (
        (AGREE_STATUS, 'Agree'),
        (DENY_STATUS, 'Deny'),
        (PENDING_STATUS, 'Pending'),
        )
    contact = models.OneToOneField(Contact)
    room = models.OneToOneField(MeetingRoom)
    book_date = models.DateTimeField()
    book_time = models.IntegerField(choices=TIME_CHOICE, default=AM)
    subscribe_time = models.DateTimeField(auto_now_add=True)
    vip = models.CharField(max_length=256)
    status = models.IntegerField(choices=STATUS_CHOICE, default=AGREE_STATUS)
    def __unicode__(self):
        return '%s, %s' % (self.contact.name, self.room.name)