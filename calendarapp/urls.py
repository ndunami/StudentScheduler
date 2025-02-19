from django.urls import path

from .views import index, prep_events, upload_calendar


urlpatterns = [
    path("", index, name="index"),
    path("api/get-calendar/", prep_events, name="prep_events"),
    path("upload-calendar/", upload_calendar, name="upload_calendar"),
] 