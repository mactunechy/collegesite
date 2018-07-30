from django import forms

from .models import Tutorial

class TutorialForm(forms.ModelForm):
	class Meta:
		model = Tutorial
		fields = ('topic','lecturer','cover_image', 'description','video','resources','prize')
