# Generated by Django 4.0.6 on 2022-08-01 23:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Contact phone number', max_length=128, region=None, unique=True),
        ),
    ]