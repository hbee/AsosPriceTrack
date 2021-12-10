from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('url', )




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]