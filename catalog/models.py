from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


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
    id = models.AutoField(auto_created=True,
                          primary_key=True,
                          serialize=False,
                          verbose_name='ID')

    title = models.CharField(max_length=200)

    date = models.DateTimeField(blank=True)

    # Foreign Key
    leader = models.ForeignKey('Leader',
                               on_delete=models.SET_NULL, null=True)

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


class Leader(models.Model):
    id = models.AutoField(auto_created=True,
                          primary_key=True,
                          serialize=False,
                          verbose_name='ID')

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(max_length=254)

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
