from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, ProfileUpdateForm,UserUpdateForm
from .models import Profile
from django.contrib.auth.models import User
from competitions.models import Competitions

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def changeprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        competitions = Competitions.objects.all()
        users = Profile.objects.all().order_by('-rating')
    context={
        'u_form':u_form,
        'p_form':p_form,
        "users": users,
        "competitions": competitions
    }
    return render(request,'users/changeprofile.html',context)

@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    competitions = Competitions.objects.all()
    users = Profile.objects.all().order_by('-rating')
    print(profile,'profile')
    context={
        "profile": profile,
        "user": user,
        "users": users,
        "competitions": competitions
    }
    return render(request,'users/profile.html',context)