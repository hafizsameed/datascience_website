# Generated by Django 3.0.5 on 2020-04-19 21:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('prob_Description', models.TextField()),
                ('file_detail', models.TextField()),
                ('evaluation', models.TextField()),
                ('difficulty', models.CharField(default='', max_length=1)),
                ('submissions', models.ManyToManyField(blank=True, to='competitions.Submission')),
            ],
        ),
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=7200))),
                ('questions', models.ManyToManyField(to='competitions.Question')),
                ('registrations', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
