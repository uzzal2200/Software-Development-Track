
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]


class ChangeInfo(UserChangeForm):
    password=None
    email=forms.EmailField(disabled=True)
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
