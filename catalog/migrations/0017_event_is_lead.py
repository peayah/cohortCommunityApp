# Generated by Django 4.0.6 on 2022-08-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_eventinstance_attendee'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_lead',
            field=models.CharField(blank=True, choices=[('t', 'Teaching'), ('n', 'Not teaching')], default='n', max_length=1),
        ),
    ]
