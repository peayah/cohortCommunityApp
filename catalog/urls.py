from django.urls import path
from . import views
from .views import EventListView, AboutPageView, IndexPageView


urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("events/", views.EventListView.as_view(), name="events"),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path("leaders/", views.LeaderListView.as_view(), name="leaders"),
    path('leader/<int:pk>', views.LeaderDetailView.as_view(), name='leader-detail'),
    path('myevents/', views.AttendedEventByUserListView.as_view(), name='my-attending'),
    path('mycohorts/', views.Cohort_and_Attendees_List_View.as_view(), name='my-leading'),
]
