from django.urls import path
from .views import index, RegisterView, prep_events


urlpatterns = [
    path("", index, name="index"),
    path("api/get-calendar/", prep_events, name="prep_events"),
    path('register/', RegisterView.as_view(), name='users-register')

]