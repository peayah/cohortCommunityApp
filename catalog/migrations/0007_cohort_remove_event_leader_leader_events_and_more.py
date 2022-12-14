# Generated by Django 4.0.6 on 2022-08-03 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_event_attendees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='leader',
        ),
        migrations.AddField(
            model_name='leader',
            name='events',
            field=models.ManyToManyField(related_name='leader', through='catalog.Cohort', to='catalog.event'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('m_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cohorts', models.ManyToManyField(to='catalog.cohort')),
            ],
        ),
        migrations.AddField(
            model_name='cohort',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cohorts', to='catalog.event'),
        ),
        migrations.AddField(
            model_name='cohort',
            name='leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cohorts', to='catalog.leader'),
        ),
    ]
