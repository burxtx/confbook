# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.views.generic.simple import direct_to_template
from django.views.generic import FormView

urlpatterns = patterns('meeting.views',
    url(r'^agreed_list$', 'list_agreed_reservation', name="list_agreed_reservation"),
    url(r'^pending_list$', 'review_pending_reservation_list', name="review_pending_reservation_list"),
    url(r'^available_room_list$', 'list_available_room', name="list_available_room"),
    url(r'^booking/new$', 'new_reservation', name="new_reservation"),
    url(r'^success$', 'new_reservation', name="submit_success"),
    url(r'^reservation/(\d+)$', 'reservation_detail', name="reservation_detail"),
    url(r'^reservation/review/(\d+)$', 'review_pending_reservation', name="review_pending_reservation"),
    url(r'^reservation/(\d+)/delete$', 'delete_reservation', name="delete_reservation"),
    # url(r'^all$', 'list_meetingrooms', name="list_meetingrooms"),
    # url(r'^add$', 'add_meetingroom', name="add_meetingroom"),
    # url(r'^delete$', 'delete_meetingroom', name="delete_meetingroom"),
    )