from django.urls import path

from .views import *

urlpatterns = [
    path('', ListProject.as_view(), name='home'),
]
