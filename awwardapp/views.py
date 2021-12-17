from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Profile, Project
from django.contrib.auth.models import User
from awwardapp.forms import ProfileForm, UpdateProfileForm, SignUpForm, UpdateProfileForm, UpdateUserForm, ProjectForm, showprojectform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
# from rest_framework.views import APIView
from awwardapp import serializer
# from .serializer import ProfileSerializer, ProjectSerializer
# from rest_framework.response import Response
from django.urls import reverse


def index(request):
    project = Project.objects.all().order_by('-id')
    return render(request, 'index.html',{'project':project})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)

    return render(request,"registration/profile.html",{'profile':profile,'project':project})

@login_required(login_url='/accounts/login/')
def post_project(request):
    if request.method == "POST":
        form = showprojectform(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form = showprojectform()
    return render(request, 'post_project.html', {"form": form})

def update_profile(request):
    current_user= request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    form=UpdateProfileForm()
    if request.method=='POST':
        form=UpdateProfileForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            redirect("/profile")
    
    return render(request, "registration/update_profile.html", {"form":form, "profile":profile})

def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})   

def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, "project_details.html", {"project": project})  

@login_required(login_url='/accounts/login/')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        projects = Project.search_project_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'found': message, 'projects': projects})
    else:
        message = 'Not found'
        return render(request, 'search.html', {'danger': message})   

# class ProjectList(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#     def get(self,request,format=None):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects,many=True)
#         return Response(serializer.data)

# class ProfileList(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#     def get(self,request,format=None):
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles,many=True)
#         return Response(serializer.data) 