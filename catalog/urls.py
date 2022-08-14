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

    path('eventinstance/<int:pk>/update/', views.EventInstanceUpdate.as_view(),
         name='event-instance-update'),
    path('eventinstance/<int:pk>/delete/', views.EventInstanceDelete.as_view(),
         name='event-instance-delete'),

    path('event/create/', views.EventCreate.as_view(), name='event-create'),
    path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
]
