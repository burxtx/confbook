# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.views.generic.simple import direct_to_template
from django.views.generic import FormView

urlpatterns = patterns('meeting.views',
    url(r'^reservation/(.+)$', 'room_detail', name="room_detail"),
    url(r'^agree$', 'list_agreed_reservation', name="list_agreed_reservation"),
    url(r'^review$', 'review_pending_reservation', name="review_pending_reservation"),
    url(r'^available_list$', 'list_available_room', name="list_available_room"),
    url(r'^booking/new$', 'new_reservation', name="new_reservation"),
    # url(r'^all$', 'list_meetingrooms', name="list_meetingrooms"),
    # url(r'^add$', 'add_meetingroom', name="add_meetingroom"),
    # url(r'^delete$', 'delete_meetingroom', name="delete_meetingroom"),
    )