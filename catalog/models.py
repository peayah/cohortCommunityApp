from django.db import models
from django.urls import reverse


class Level(models.Model):

    level_type = models.CharField(max_length=200,
                                  help_text='Enter Level (Beginner, All, Specialized)')

    def __str__(self):
        return self.level_type


class Language(models.Model):
    language_type = models.CharField(max_length=200,
                                     help_text='Enter Language (HTML, CSS, '
                                               'JavaScript, Data, API)')

    def __str__(self):
        return self.language_type


class Event(models.Model):

    title = models.CharField(max_length=200)

    date = models.DateField(null=True, blank=True)

    # Foreign Key
    leader = models.ForeignKey('Leader',
                               on_delete=models.SET_NULL, null=True)

    description = models.TextField(max_length=1000,
                                   help_text='Enter a brief description of tevent')

    level = models.ManyToManyField(Level,
                                   help_text='Select a level for this event')

    image = models.ImageField(upload_to='images')

    def __str__(self):f
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])
