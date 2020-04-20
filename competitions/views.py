from django.shortcuts import render,redirect
from .models import Competitions,Question,Submission
from django.contrib.auth.models import User
from users.models import Profile
import datetime
from django.views.generic import DetailView
from .form import SubmissionForm
from django.contrib import messages


def home(request):
        competions = Competitions.objects.all()
        users = Profile.objects.all().order_by('-rating')
        context={
                "competitions":competions,
                "users":users
        }
        return render(request,'competitions/home.html',context)

def contests(request):
        competitions = Competitions.objects.all()
        old=[]
        upcoming=[]
        for comp in competitions:
                date = datetime.datetime.now(datetime.timezone.utc)
                diff = comp.start_time - date
                if diff.days < 0:
                        old.append(comp)
                else:
                        upcoming.append(comp)

        context={
                "upcoming": upcoming,
                "old":old
        }
        return render(request,'competitions/contests.html',context)

class CompetitionDetailView(DetailView):
        model= Competitions

class QuestionDetailView(DetailView):
        model = Question


def questionDetail(request,param1,param2):
        compid = param1
        question_id = param2
        comp = Competitions.objects.filter(id=compid).first()
        question = Question.objects.filter(id=question_id).first()
        if request.method == 'POST':
                print("post request")
                form = SubmissionForm(request.POST,request.FILES)
                if form.is_valid():
                        print("form is valid")
                        obj = form.save(commit=False)
                        obj.user = request.user
                        obj.save()
                        subs = question.submission_list
                        subs.append(obj)
                        question.submissions.set(subs)
                        question.save()
                        quests = comp.question_list
                        newQuests = []
                        for q in quests:
                                if q.title == question.title:
                                         newQuests.append(question)
                                else:
                                        newQuests.append(q)
                        comp.questions.set(newQuests)
                        comp.save()
                        messages.success(request, f'submitted')
                        return redirect('question-detail',compid,question_id)
        form = SubmissionForm()
        context={
                "comp": comp,
                "question": question,
                "form": form
        }
        return render(request,'competitions/question_detail.html',context)

def register(request,param1):
        current_competition = Competitions.objects.filter(id=param1).first()
        if request.method == 'POST':
                registers = current_competition.reg_list
                registers.append(request.user)
                current_competition.registrations.set(registers)
                messages.success(request, f'registered successfully')
                return redirect('contests')
        users = User.objects.all()
        current_competition = Competitions.objects.filter(id=param1).first()
        competions = Competitions.objects.all()
        print(current_competition)
        context={
                "competitions":competions,
                "users":users,
                "curr_comp": current_competition
        }
        return render(request,'competitions/register.html',context)

def ratings(request):
        competions = Competitions.objects.all()
        users = Profile.objects.all().order_by('-rating')

        context = {
                "competitions": competions,
                "users": users
        }
        return render(request,'competitions/ratings.html',context)