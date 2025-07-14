# ---------------------- Django HTML Views ---------------------- #
from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'core/home.html', {'projects': projects, 'skills': skills})

def about(request):
    return render(request, 'core/about.html')

# (Optional) contact view for your contact page
def contact(request):
    return render(request, 'core/contact.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {'projects': projects})


# ---------------- Django REST Framework API ViewSets ---------------- #
from rest_framework import viewsets
from .models import Project, Skill, ContactMessage
from core.serializers import ProjectSerializer, SkillSerializer, ContactSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer