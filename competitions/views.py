from django.shortcuts import render,redirect
from .models import Competitions,Question,Submission
from django.contrib.auth.models import User
from users.models import Profile
import datetime
from django.views.generic import DetailView
from .form import SubmissionForm
from django.contrib import messages
from django.core.exceptions import SuspiciousOperation
from .tasks import hello_world

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
        reg_upcoming=[]
        not_reg_upcoming=[]
        for comp in competitions:
                date = datetime.datetime.now(datetime.timezone.utc)
                diff = comp.end_time - date
                if diff.days < 0:
                        old.append(comp)
                else:
                        if comp.is_registered(user=request.user):
                                reg_upcoming.append(comp)
                        else:        
                                not_reg_upcoming.append(comp)

        context={
                "not_reg_upcoming":not_reg_upcoming,
                "reg_upcoming": reg_upcoming,
                "old":old
        }
        return render(request,'competitions/contests.html',context)

# class CompetitionDetailView(DetailView):
#         model= Competitions

def competitionDetailView(request,param1):
        compid = param1
        comp = Competitions.objects.filter(id=compid).first()
        date = datetime.datetime.now(datetime.timezone.utc)
        diff = comp.start_time - date
        print(diff,'diff')
        context={
                        'comp':comp
                }
        if diff.days > 0:
                messages.warning(request, f'Invalid Request')
                return redirect('contests')
        elif not comp.is_registered(request.user):
                messages.warning(request, f'You are not registered to this contest')
                return redirect('contests')
        else:
                return render(request,'competitions/competitions_detail.html',context)

class QuestionDetailView(DetailView):
        model = Question


def questionDetail(request,param1,param2):
        compid = param1
        question_id = param2
        comp = Competitions.objects.filter(id=compid).first()
        question = Question.objects.filter(id=question_id).first()
        if request.method == 'POST':
                print("post request",request.POST['url'])
                url = request.POST['url']
                form = SubmissionForm(request.POST,request.FILES)
                if form.is_valid():
                        print("form is valid")
                        obj = form.save(commit=False)
                        obj.user = request.user
                        obj.competition = comp
                        obj.question = question
                        obj.save()
                        print(obj.user.username,'username')
                        messages.success(request, f'submitted')
                        request.session['compid']=compid
                        request.session['question_id']= question_id
                        request.session['url'] = url
                        print('form submitted')
                        return redirect('my-submissions',compid)
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

def mysubmissions(request,param1):
        compid = param1
        # result= hello_world.delay()
        # print(result,'result')
        comp = Competitions.objects.filter(id=compid).first()
        submissions = Submission.objects.filter(user=request.user, competition=comp).order_by('-time')
        context={
                'comp':comp,
                'submissions':submissions
        }
        return render(request,'competitions/mysubmissions.html',context)