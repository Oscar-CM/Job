from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField()
    firstname = forms.CharField()
    lastname = forms.CharField()

    class Meta:
        model = User
        fields = ['firstname','lastname', 'username','phone', 'email','password1', 'password2']
