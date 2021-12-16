
from .models import Profile,Project
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class showprojectform(ModelForm):
    class Meta:
        model=Project
        fields=('image',
                'title',
                'description',
                'category',
                'location',
                 'url',
               )

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','contact') 

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'profile', 'date']