from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Application
from django.urls import reverse_lazy

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    template_name = 'application/apply.html'
    fields = ['title', 'profile', 'cv']
    success_url = reverse_lazy('application-list')

class ApplicationListView(ListView):
    model = Application
    context_object_name = 'posts'

    template_name = 'application/applications.html'


