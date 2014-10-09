# coding: utf-8
from django import forms
from django.forms import ModelForm
from meeting import MeetingRoom

class MeetingRoomSaveForm(forms.Form):
    name = forms.CharField(
        widget = forms.TextInput(attrs={'size': 64})
        )

class BookRoomForm(forms.Form):
    name = forms.CharField(
        widget = forms.TextInput(attrs={'size': 64})
        )
    phone = forms.IntegerField(
        widget = forms.TextInput(attrs={'size': 11})
        )
    dept = forms.CharField(
        widget = forms.TextInput(attrs={'size': 128})
        )
    room = forms.CharField(
        widget = forms.SelectInput())
    date = forms.DateField(
        widget = forms.TextInput(initial=datetime.date.today)
        )

# class MeetingRoomSaveForm(ModelForm):
#     class Meta:
#         model = MeetingRoom
#         fields = ['name']
# class BookRoomForm(ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['name', 'room', 'book_date', 'book_time']