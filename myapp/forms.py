from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

METRIC_CHOICES = [
    ( 1, 'Past 24hours'),
    ( 7, 'Past Week'),
    ( 30, 'Past Months'),
    ( 31, 'Older'),
]

class MetricForm(forms.Form):
    day = forms.ChoiceField(choices=METRIC_CHOICES)

class MailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject', 'size': 30}))
    content = forms.CharField(widget=forms.Textarea(attrs={
            'placeholder': 'Message', 'cols':30, 'rows': 5 })) 
        
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

