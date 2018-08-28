from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [
	path('new', views.TutorialCreateView.as_view(),name='tutorial_create'),
	path('update/<slug:username>/<slug:slug>',views.TutorialUpdateView.as_view(),name='tutorial_update'),
	path('delete/<slug:username>/<slug:slug>',views.TutorialDeleteView.as_view(),name='tutorial_delete'),
		path('',views.CourseListView.as_view(),name='tutorial_list'),
		path('<slug>',views.CourseDetailView.as_view(),name='course_detail'),	
		path('enroll/<pk>',views.enroll,name="enroll")



]