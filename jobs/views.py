from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post



def home(request):
    return render(request, 'jobs/home.html')

class PostListView(ListView):
    model = Post
    template_name = 'jobs/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'jobs/datail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'jobs/post_form.html'
    fields = ['company', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'jobs/post_form.html'
    fields = ['company', 'title', 'content']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'jobs/delete.html'
    success_url = '/home/findjob'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def postjob(request):

    return render(request, 'jobs/postjob.html')

def findjob(request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'jobs/findjob.html', context)
def about(request):

    return render(request, 'jobs/about.html')
def contact(request):

    return render(request, 'jobs/contactus.html')
# Create your views here.
