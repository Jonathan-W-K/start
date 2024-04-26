from django import forms
from .models import Myuser, Student


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Myuser
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentname', 'email', 'password', 'age']
        widgets = {'password': forms.PasswordInput()}


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentname', 'email', 'age']
