# Generated by Django 4.0.6 on 2022-08-04 02:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_cohort_borrower'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('a', 'Attending'), ('w', 'Waitlist'), ('n', 'Not Attending')], default='n', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='cohorts',
        ),
        migrations.RemoveField(
            model_name='leader',
            name='events',
        ),
        migrations.AddField(
            model_name='event',
            name='leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.leader'),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Cohort',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='eventinstance',
            name='cohort',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.event'),
        ),
    ]