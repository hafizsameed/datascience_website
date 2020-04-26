from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import datetime



class Question(models.Model):
    title = models.CharField(max_length=100)
    prob_Description = models.TextField()
    file_detail = models.TextField()
    evaluation = models.TextField()
    difficulty = models.CharField(max_length=1 , default='')
    # submissions = models.ManyToManyField(Submission,blank=True)
    # @property
    # def submission_list(self):
    #     return list(self.submissions.all())

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
    def started(self):
        date = datetime.datetime.now(datetime.timezone.utc)
        start_diff = date - self.start_time
        print(start_diff,'start_diff')
        end_diff = self.end_time - date
        print(end_diff,'end_diff')
        hrs = self.duration.seconds
        print(hrs,'hrs')
        print(start_diff.seconds,'diff end')
        if start_diff.days == 0 and start_diff.seconds < hrs  :
            return True
        else:
            return False

    def is_registered(self,user):
        reg_list = self.reg_list
        for i in  reg_list:
            if i.username==user.username:
                return True
        return False


    def __str__(self):
        return self.title

class Submission(models.Model):
    file = models.FileField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    time = models.DateTimeField(default=timezone.now)
    verdict = models.CharField(blank=True,default='',max_length=30)
    point = models.IntegerField(null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,null=True)
    competition = models.ForeignKey(Competitions,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.id) + self.user.username

class Ranking(models.Model):
    competition = models.OneToOneField(Competitions,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    submissions = models.ManyToManyField(Submission,max_length=4)
    totalpoints = models.IntegerField(blank=True)

