
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('postjob', views.postjob,name = 'postjob'),
    path('findjob', views.findjob,name = 'findjob'),
    path('about', views.about,name = 'about'),
    path('contact', views.contact,name = 'contact'),
]
