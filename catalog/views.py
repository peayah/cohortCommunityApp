from django.views.generic import TemplateView
from django.views import generic
from catalog.models import Leader
from catalog.models import Event


class IndexPageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class EventListView(generic.ListView):
    template_name = "events.html"
    model = Event
    context_object_name = 'event_list'
    paginate_by = 10

    # queryset = Event.objects.filter(title__icontains='API')[
    #            :5]  # Get 5 events containing the title API


class EventDetailView(generic.DetailView):
    template_name = "event_detail.html"
    model = Event


class LeaderListView(generic.ListView):
    template_name = "leaders.html"
    model = Leader
    context_object_name = "leader_list"
    paginate_by = 5


class LeaderDetailView(generic.DetailView):
    template_name = "leader_detail.html"
    model = Leader