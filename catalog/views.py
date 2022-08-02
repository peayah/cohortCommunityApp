from django.shortcuts import render

# Create your views here.
from .models import Event, Leader, Level, Language

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_events = Event.objects.all().count()

    # The 'all()' is implied by default.
    num_leaders = Leader.objects.count()

    num_levels = Level.objects.count()

    num_language = Language.objects.count()


    context = {
        'num_books': num_events,
        'num_leaders': num_leaders,
        'num_levels': num_levels,
        'num_language': num_language,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)