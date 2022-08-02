from django.views.generic import TemplateView
from django.views import generic

from catalog.models import Event


class IndexPageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class EventListView(generic.ListView):
    template_name = "events.html"
    model = Event
    context_object_name = 'event_list'
    queryset = Event.objects.filter(title__icontains='API')[
               :5]  # Get 5 events containing the title API

