from django.views.generic import TemplateView
from allauth.account import views
class HomePage(TemplateView):
	template_name = 'collegesite/index.html'
	
	
class ThanksPage(TemplateView):
	template_name = 'collegesite/thanks.html'
	
class WelcomePage(TemplateView):
	template_name = 'collegesite/welcome.html'
	
#class LoginPage(TemplateView):
	# template_name = 'collegesite/login.html'	
	
	
class LoginPage(views.LoginView):
	template_name = 'accounts/login.html'	
	
	
class 	LogoutPage(views.LogoutView):
	template_name="accounts/logout"
	
	
class SignupPage(views.SignupView):
	template_name	="accounts/signup.html"