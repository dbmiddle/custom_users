from django import forms
from custom_users.models import MyUser
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'display_name'
        ]
    # display_name = forms.CharField(max_length=50, null=True, blank=True)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)