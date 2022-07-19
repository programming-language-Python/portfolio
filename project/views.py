# Create your views here.
from django.views.generic import ListView

from project.models import Project


class ListProject(ListView):
    model = Project


class ProjectsByLanguage(ListView):

    def get_queryset(self):
        return Project.objects.filter(language_id=self.kwargs['language_id']).select_related(
            'language')
