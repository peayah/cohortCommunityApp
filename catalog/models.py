from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User, AbstractUser
import uuid


class Event(models.Model):

    title = models.CharField(max_length=200)

    date = models.DateTimeField(blank=True)

    attendees = models.IntegerField(default=20)

    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    STATUS = (
        ('t', 'Teaching'),
        ('n', 'Not Teaching'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='t',
    )

    description = models.TextField(max_length=1000, help_text='Enter a brief description of tevent')

    LEVEL_CHOICES = (
        ('all levels', 'ALL'),
        ('beginner', 'BEGINNER'),
        ('specialized', 'SPECIALIZED'),
    )

    level = models.CharField(max_length=15, choices=LEVEL_CHOICES, default='all')

    LANGUAGE_CHOICES = (
        ('api', 'API'),
        ('css', 'CSS'),
        ('data', 'DATA'),
        ('html', 'HTML'),
        ('javascript', 'JAVASCRIPT'),
    )

    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES, default='html')

    image = models.ImageField(upload_to='static/img/')

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class EventInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    leader = models.ForeignKey('Leader', on_delete=models.RESTRICT, null=True)

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
        default='a',
    )

    def __str__(self):
        return f'{self.id} ({self.cohort.title})'

    # def get_absolute_url(self):
    #     return reverse('event-detail', args=[str(self.id)])


class Leader(models.Model):

    leader = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               null=True)

    phone = PhoneNumberField(null=False,
                             blank=False,
                             unique=True,
                             help_text='Contact phone number')

    def get_absolute_url(self):
        return reverse('leader-detail', args=[str(self.id)])

    # def __str__(self):
    #     return f'{first_name} {self.last_name}'
