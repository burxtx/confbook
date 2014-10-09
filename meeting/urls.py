# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.views.generic.simple import direct_to_template
from django.views.generic import FormView

urlpatterns = patterns('meeting.views',
    url(r'^(?P<year>\d[4])/(?P<month>\d[2])/(?P<day>\d[2])/(?P<status>\w[.+])$', 'filter_rooms', name="filter_rooms"),
    url(r'^booking/$', 'book_meetingroom', name="book_meetingroom"),
    url(r'^(.+)/detail$', 'room_detail', name="room_detail"),
    url(r'^review$', 'review_submits', name="review_submits"),
    # url(r'^all$', 'list_meetingrooms', name="list_meetingrooms"),
    # url(r'^add$', 'add_meetingroom', name="add_meetingroom"),
    # url(r'^delete$', 'delete_meetingroom', name="delete_meetingroom"),
    )