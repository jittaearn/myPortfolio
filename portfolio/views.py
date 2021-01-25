from random import sample
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .forms import CommentForm
from .models import Comment
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

# def get_form(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = CommentForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             form.save()

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = CommentForm()

#     return render(request, 'form.html', {'form': form})


class ContactView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = CommentForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
