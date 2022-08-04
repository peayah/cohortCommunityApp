from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User, AbstractUser
import uuid


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

    date = models.DateTimeField(blank=True)

    attendees = models.IntegerField(default=20)

    leader = models.ForeignKey('Leader',
                                        on_delete=models.SET_NULL,
                                        null=True)

    description = models.TextField(max_length=1000,
                                   help_text='Enter a brief description of tevent')

    level = models.ManyToManyField(Level,
                                   help_text='Select a level for this event')

    language = models.ManyToManyField(Language,
                                      help_text='Select a language for this event')

    image = models.ImageField(upload_to='static/img/')

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])


    def __str__(self):
        return self.title


class EventInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    cohort = models.ForeignKey('Event', on_delete=models.RESTRICT, null=True)

    attendee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    STATUS = (
        ('a', 'Attending'),
        ('w', 'Waitlist'),
        ('n', 'Not Attending'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='n',
    )

    def __str__(self):
        return f'{self.id} ({self.cohort.title})'

    # def get_absolute_url(self):
    #     return reverse('event-detail', args=[str(self.id)])





class Leader(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(max_length=254,
                             unique=True)

    phone = PhoneNumberField(null=False,
                             blank=False,
                             unique=True,
                             help_text='Contact phone number')

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('leader-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
