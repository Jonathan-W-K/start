from django import forms
from .models import User, Student


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentname', 'age']
        widgets = {'password': forms.PasswordInput()}


# class RegistrationForm(forms.ModelForm):
#  class Meta:
#     model = Student  # Change this to Student model if you're registering students
#     fields = ['username', 'email', 'password']
#     widgets = {'password': forms.PasswordInput()}


"""
from django import forms
from .models import Myuser, Student, Registration


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Myuser
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentname', 'email', 'password', 'age']
        widgets = {'password': forms.PasswordInput()}


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Myuser  # Assuming you want to register users, so using Myuser model
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")



from django import forms
from .models import Myuser, Student, Registration


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



class StudentDeleteForm(forms):
    class Meta:
        model = Student
        fields = ['studentname', 'email', 'age']



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentname', 'email', 'age']
"""

"""
from django import forms
from .models import Myuser, Student, Registration


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Myuser
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentname', 'email', 'password', 'age']
        widgets = {'password': forms.PasswordInput()}


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Myuser  # Assuming you want to register users, so using Myuser model
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")



from django import forms
from .models import Myuser, Student, Registration


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



class StudentDeleteForm(forms):
    class Meta:
        model = Student
        fields = ['studentname', 'email', 'age']



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentname', 'email', 'age']
"""
