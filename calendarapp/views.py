from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from icalendar import Calendar
from json import dumps
import common.util

# Create your views here.
def index(request):
    return render(request, "calendarapp/calendar.html")



@api_view(['GET'])
def prep_events(request) -> list:
    """
    This function loops over the list of calendar events, and handles rrules for repetition.
    """
    ics_content = common.util.preprocess_ics("calendarTest.ics")

    calendar = Calendar.from_ical(ics_content)

    events = common.util.processRrule(calendar)
    return HttpResponse(dumps(events))
