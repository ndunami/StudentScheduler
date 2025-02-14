from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view

from icalendar import Calendar
from json import dumps

from common.util import preprocess_ics, processRrule


# Create your views here.
def index(request):
    return render(request, "calendarapp/calendar.html")


@api_view(['GET'])
def prep_events(request):
    """
    This function loops over the list of calendar events, and handles rrules for repetition.
    """
    calendar = Calendar.from_ical(preprocess_ics("calendarTest.ics"))
    events = processRrule(calendar)

    return HttpResponse(dumps(events))
