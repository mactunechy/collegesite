from django.urls import path

from . import views
app_name="dashboard"

urlpatterns = [
		path('<slug>',views.dashboard,name="home"),
		path('<slug>/<slug:slug1>/<int:pk>',views.course_detail,name="course_detail")



			]
			
			