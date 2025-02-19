from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import CalendarUploadForm
from .models import Calendar

from rest_framework.decorators import api_view

from icalendar import Calendar
from json import dumps

from common.util import preprocess_ics, processRrule


# Create your views here.
def index(request):
    return render(request, "calendarapp/calendar.html")

@login_required
def upload_calendar(request):
    if request.method == "POST":
        form = CalendarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.user = request.user
            calendar.save()
            return redirect(to="/")
    else:
        form = CalendarUploadForm
    return render(request, "calendarapp/upload_calendar.html", {"form": form})

@api_view(['GET'])
def prep_events(request):
    """
    This function loops over the list of calendar events, and handles rrules for repetition.
    """
    calendar = Calendar.from_ical(preprocess_ics("calendarTest.ics"))
    events = processRrule(calendar)

    return HttpResponse(dumps(events))
