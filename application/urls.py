
from django.urls import path
from .views import ApplicationCreateView, ApplicationListView
from . import views

urlpatterns = [
    path('', ApplicationCreateView.as_view(),name = 'application-home'),
    path('list/', ApplicationListView.as_view(),name = 'application-list'),

]
