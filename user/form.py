from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "firstName", "lastName", "password1", "password2", "role")
