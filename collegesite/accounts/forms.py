from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ("profile_pic","membership")
				
	
	
class UserCreateForm(UserCreationForm):
     
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
            'password1':"enter correct password ",
            'password2':None,
        }	