from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)               # creates field for form
    email = forms.EmailField(required=True)
    fName = forms.CharField(label = 'First Name',max_length=150)
    lName = forms.CharField(label = 'Last Name',max_length=150)
    Type = forms.ChoiceField(choices=(('staff','Staff'),('student','Student')), widget=forms.RadioSelect)
    Role = forms.ChoiceField(choices=(('user','User'),('admin','Admin')), widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'fName', 'lName', 'password1', 'Type', 'Role', 'password2']      # for layout of the form