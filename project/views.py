# Create your views here.
from django.views.generic import ListView

from project.models import Project


class ListProject(ListView):
    model = Project
