# coding: utf-8
from django.shortcuts import render
import time, datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.core.urlresolvers import reverse
from meeting.models import *
import pdb

pdb.set_trace()
# I am common user, I want to book a meeting room
def _save_reservation(request):
    meetingroom = MeetingRoom.objects.get(name=request.POST['room'])
    person, created = Contact.objects.get_or_create(phone=request.POST['phone'])
    if created:
        person.name = request.POST['name']
        person.phone = request.POST['phone']
        person.dept = request.POST['dept']
    person.save()
    rsv = Reservation()
    rsv.contact = person
    rsv.room = meetingroom
    rsv.book_date = request.POST['date']
    rsv.book_time = request.POST['time']
    rsv.vip = request.POST['vip']
    rsv.count = request.POST['count']
    rsv.status = Reservation.PENDING_STATUS
    rsv.save()
    return rsv

def new_reservation(request):
    # post booking request
    if request.method == 'POST':
        if "submit_pending" in request.POST:
        # validate forms firstly
        # create a booking request
            rsv = _save_reservation(request)
        return render_to_response('meeting/submit_success.html', variables)
    # open the booking request page
    else:
        date = request.GET.get('date')
        time_slot = request.GET.get('time_slot')
        variables = RequestContext(request, {
            'meetingrooms': date,
            'time': time,
            })
    return render_to_response('meeting/book_new_room.html', variables)


#---------- pending following functions-------------
# # I am admin, I want to add new meeting rooms
# def list_meetingrooms(request):
#     meetingrooms = MeetingRoom.objects.all()
#     variables = RequestContext(request, {
#         'meetingrooms': meetingrooms,
#         })
#     return render_to_response('meeting/room_list.html', variables)

# def add_meetingroom(request, id=None):
#     if request.GET.has_key('ajax'):
#         meetingroom, created = MeetingRoom.objects.get_or_create(pk=id)

# def delete_meetingroom(request, id=None):
#     mr = get_object_or_404(MeetingRoom, pk=id)
#     mr.delete()
#     results={'success': True}
#     json = simplejson.dumps(results)
#     # return HttpResponse()
#     # return HttpResponse(json, mimetype='application/json')
#     if request.is_ajax():
#         return HttpResponse(json, mimetype='application/json')
#     # else:
#     #     return HttpResponseRedirect('/user/%s/' % username)
#     # return HttpResponseRedirect(reverse('user_page', args=(username,)))
#     # return HttpResponseRedirect('/user/%s/' % username)
#---------------------the end-----------

# I am admin, I want to review someday's booking requests
# def review_submits(request, date):
#     if request.method=='GET':
#         meetingrooms = MeetingRoom.objects.exclude(
#             reservation__status=Reservation.PENDING_STATUS,
#             book_date=date)
#     variables = RequestContext(request, {
#         'meetingrooms': meetingrooms,
#         })
#     return render_to_response('meeting/reservation_list.html', variables)
    
# I am common user, I want to view someday's rooms
def list_agreed_reservation(request):
    date = request.GET.get('date')
    # I am common user I want to view someday's meetings
    if request.method=='GET':
        rsvs = Reservation.objects.filter(
            status=Reservation.AGREE_STATUS,
            book_date=date)
        variables = RequestContext(request, {
            'rsvs': rsvs,
            })
        return render_to_response('meeting/agreed_reservation_list.html', variables)

# I am admin I want to approve someday's booking requests
def review_pending_reservation(request):
    date = request.GET.get('date')
    if request.method=='GET':
        rsvs = Reservation.objects.filter(
            status=Reservation.PENDING_STATUS,
            book_date=date)
        variables = RequestContext(request, {
            'rsvs': rsvs,
            })
        return render_to_response('meeting/pending_reservation_list.html', variables)

# I am common user I want to book someday's meeting room
def list_available_room(request):
    date = request.GET.get('date')
    time_slot = request.GET.get('time_slot')
    print 'now ====',
    print request.GET
    if request.method=='GET':
        meetingrooms = MeetingRoom.objects.exclude(
            reservation__status=Reservation.AGREE_STATUS).filter(
            reservation__book_date=date, reservation__book_time=time_slot)
        variables = RequestContext(request, {
            'meetingrooms': meetingrooms,
            'show_control': True,
            })
        return render_to_response('meeting/available_room_list.html', variables)

# I am common user, I want to view a resevered room
def room_detail(request, date, time, id):
    room = get_object_or_404(MeetingRoom, pk=id)
    if room:
        reservation = room.reservation_set.filter(book_date=date, book_time=time)
    variables = RequestContext(request, {
        'name': reservation.contact.name,
        'phone': reservation.contact.phone,
        'book_date': reservation.date,
        'book_time': reservation.time,
        'vip': reservation.vip,
        'status': reservation.status,
        })
    return render_to_response('meeting/room_detail.html', variables)