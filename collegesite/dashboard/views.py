from django.shortcuts import render,get_object_or_404
from tutorials.models import Course,Registered_student
from django.views import generic
from django.db.models import Q
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()
def dashboard(request,slug):
	my_courses = Course.objects.filter(enrolled_students__student__username__icontains=slug)
	template_name = "dashboard/home.html"
#	print(my_courses)
	context = {
		"my_courses":my_courses
	}
	return render(request,template_name,context)
	
	
def course_detail(request,slug,slug1,pk):
	course=get_object_or_404(Course,slug=slug1)
	
	user = get_object_or_404(User,username=slug)
	
	registered_student=Registered_student.objects.filter(Q(course=course) and Q(student=user))
	print(registered_student)
	template_name = "dashboard/course_detail.html"
	current_video = registered_student.course.tutorials.get(position=pk)
	context = {
			'course':registered_student.course,
			'current_video':current_video
	}
	return render(request,template_name,context)