from django.shortcuts import render

jobs = [
    {
        'author': 'Oscar',
        'title': 'Computer science',
        'content': 'A jo for any computer scienttist ooking for an internship position',
        'date_posted': 'February 16 2020'
    },
    {
        'author': ' Limo',
        'title': 'Information technology',
        'content': 'A job for any computer scientist looking for an internship position',
        'date_posted': 'February 10 2020'
    }
]


def home(request):
    return render(request, 'jobs/home.html')


def postjob(request):

    return render(request, 'jobs/postjob.html')
def findjob(request):
    context = {
        'jobs': jobs
    }
    return render (request, 'jobs/findjob.html', context)
def about(request):

    return render(request, 'jobs/about.html')
def contact(request):

    return render(request, 'jobs/contactus.html')
# Create your views here.
