from django.urls import path

from . import views
from .forms import CommentForm

app_name = 'portfolio'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('experience/', views.ExperienceView.as_view(), name='experience'),
    path('extraCurriculum/', views.ExtraCurriculumView.as_view(), name='extraCurriculum'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]