from django.db import models


class Level(models.Model):

    level_type = models.CharField(max_length=200,
                            help_text='Enter Level (Beginner, All, Specialized)')

    def __str__(self):
        return self.level_type


class Laguage(models.Model):
    language_type = models.CharField(max_length=200,
                                  help_text='Enter Language (HTML, CSS, JavaScript, Data, API)')

    def __str__(self):
        return self.language_type