from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Submission(models.Model):
    file = models.FileField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Question(models.Model):
    title = models.CharField(max_length=100)
    prob_Description = models.TextField()
    file_detail = models.TextField()
    evaluation = models.TextField()
    difficulty = models.CharField(max_length=1 , default='')
    submissions = models.ManyToManyField(Submission,blank=True)
    @property
    def submission_list(self):
        return list(self.submissions.all())

    def __str__(self):
        return self.title



class Competitions(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    start_time = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(default=datetime.timedelta(hours=2))
    registrations = models.ManyToManyField(User,blank=True)
    questions = models.ManyToManyField(Question)

    @property
    def end_time(self):
        time = self.start_time + self.duration
        return time

    @property
    def question_list(self):
        return list(self.questions.all())

    @property
    def reg_list(self):
        return list(self.registrations.all())

    @property
    def reg_list_len(self):
        return len(list(self.registrations.all()))

    @property
    def question_list(self):
        return list(self.questions.all())

    def __str__(self):
        return self.title






