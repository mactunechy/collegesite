from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy,reverse
from .forms import TutorialForm
from .models import Tutorial
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()
class TutorialDetailView(generic.DetailView):
	template_name = 'tutorials/tutorial_detail.html'
	
	
	
class TutorialListView(generic.ListView):
	model = Tutorial
	template_name= 'collegesite/index.html'
	
class TutorialDeleteView(generic.DeleteView):
	template_name = 'tutorials/tutorial_confirm_delete.html'
	model = Tutorial
	success_url = reverse_lazy('tutorial_list')
	
	
class TutorialCreateView(generic.CreateView):
	template_name = 'tutorials/tutorial_form.html'
	form_class = TutorialForm
	success_url = reverse_lazy('tutorial_detail')
	
	
class TutorialUpdateView(generic.UpdateView):
	form_class = TutorialForm
	model = Tutorial
	
	