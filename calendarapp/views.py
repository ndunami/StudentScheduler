from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views import View

from .forms import RegisterForm, LoginForm

from rest_framework.response import Response
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

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)
    