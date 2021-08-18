from datetime import timezone
from projectDemo.settings import DEFAULT_AUTO_FIELD
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'email', 'username','password1', 'password2']