from django.urls import path

from .views import *

urlpatterns = [
    path('', ListProject.as_view(), name='home'),
    path('language/<int:language_id>/',
         ProjectsByLanguage.as_view(), name='language'),
]
