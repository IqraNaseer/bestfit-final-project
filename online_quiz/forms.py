from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Feedbackk, reporting
from bestfit import settings
from django.forms.widgets import DateInput,Textarea


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [ 'birth_date','bio', 'location','gender', 'image']
        labels = {
            'birth_date': ('Dath of Birth'),
        }
        widgets = {
        'birth_date': DateInput(attrs={'type': 'date'})
    }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbackk
        fields = ['name','email','phone', 'Feedback']
        labels = {
            'Feedback': ('Give us your feedback'),
        }
        widgets = {
        'Feedback': Textarea(attrs={'rows': 3})
    }

class ReportingForm(forms.ModelForm):
    class Meta:
        model = reporting
        fields = '__all__'

        