from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def signup(request):
	if request.method == "POST":
		form = forms.UserCreateForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('new_profile')
			
		
 

	form = forms.UserCreateForm()
	context = {
		'form': form
		
	}
	template_name = 'accounts/signup.html'
	return render(request,template_name,context)
	
	
	
	
	
def new_profile(request):
	template_name = 'accounts/new_profile.html'
	if request.method == "POST":
		form = forms.ProfileForm(request.POST)
		if form.is_valid:
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('home')
	else:
		form = forms.ProfileForm()
		context = {
			'form':form
		}
		
		return render(request,template_name,context)		


	