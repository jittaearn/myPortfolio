from random import sample
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
# from .forms import QuestionForm, AnswerForm
from .models import Comment, Email
import logging

def index(request):
    #redirect user to the polls index
    return HttpResponseRedirect(reverse("portfolio:index"))


class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Comment

class ExperienceView(generic.ListView):
    template_name = 'portfolio/experience.html'
    model = Comment
    def get_queryset(self):
        """
        Return the last five published comments (not including those set to be
        published in the future).
        """
        return Comment


class ExtraCurriculumView(generic.ListView):
    template_name = 'portfolio/extraCurriculum.html'
    model = Comment
    def get_queryset(self):
        """
        Return the last five published comments (not including those set to be
        published in the future).
        """
        return Comment


class ContactView(generic.ListView):
    model = Comment
    template_name = 'portfolio/contact.html'

    def get_queryset(self):
        """
        Return the last five published comments (not including those set to be
        published in the future).
        """
        return Comment