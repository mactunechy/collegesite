from django.shortcuts import render,get_object_or_404,redirect

from django.views import generic
from django.urls import reverse_lazy,reverse
from .forms import TutorialForm
from .models import Course,Tutorial,Registered_student
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()
class TutorialDetailView(generic.DetailView):
	template_name = 'tutorials/tutorial_detail.html'
	
	
	
class CourseListView(generic.ListView):
	model = Course
	template_name= 'collegesite/index.html'
	
	
	
class CourseDetailView(generic.DetailView):
	model = Course
	template_name="tutorials/course_detail.html"	
	
	
	
def enroll(request,pk):
	course = 	get_object_or_404(Course,pk=pk)
	

	(object,created)=Registered_student.objects.get_or_create(student=request.user,course=course)
	return redirect("dashboard:course_detail",kwargs={'slug1':object.course.slug})
#	course.enrolled_students.add(request.user)
#	course.save()
#	return redirect('dashboard:course_detail')
	
	
	
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
	
	