from django.urls import path
from .views import EventListView, AboutPageView, IndexPageView


urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("events/", EventListView.as_view(), name="events"),
]