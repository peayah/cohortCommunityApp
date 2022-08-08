from django.views.generic import TemplateView
from django.views import generic
from catalog.models import Leader
from catalog.models import Event
from catalog.models import EventInstance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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


class AttendedEventByUserListView(LoginRequiredMixin, generic.ListView):
    model = EventInstance
    template_name = 'catalog/eventinstance_list_attended_by_user.html'
    paginate_by = 10

    def get_queryset(self):
        # return EventInstance.objects.filter(attendee=self.request.user).filter(
        return EventInstance.objects.filter(attendee=self.request.user).filter(
            status__exact='a')


class LeadEventByStaffListView(LoginRequiredMixin, generic.ListView):
    model = EventInstance
    template_name = 'catalog/eventinstance_list_lead_by_staff.html'
    paginate_by = 10

    def get_queryset(self):
        return EventInstance.objects.filter(cohort__leader = self.request.user).all()


class EventInstanceCreate(CreateView):
    model = EventInstance
    fields = ['cohort', 'status']


class EventInstanceUpdate(UpdateView):
    model = EventInstance
    fields = 'attending'


class EventInstanceDelete(DeleteView):
    model = EventInstance
    success_url = reverse_lazy('eventInstance')
    