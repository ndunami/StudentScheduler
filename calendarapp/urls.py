from django.urls import path

from .views import index, prep_events


urlpatterns = [
    path("", index, name="index"),
    path("api/get-calendar/", prep_events, name="prep_events"),
] 