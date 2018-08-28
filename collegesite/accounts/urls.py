from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
		path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name = "login"),
		path('logout',auth_views.LogoutView.as_view(template_name="accounts/logout"), name = "logout"),
		path('signup',views.signup, name ="signup"),
		path('signup/new_profile',views.new_profile, name ="new_profile"),
		
			]
			
			