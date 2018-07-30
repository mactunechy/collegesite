"""collegesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from . import settings
from django.views.generic import TemplateView
from tutorials.views import TutorialListView
urlpatterns = [
		path('',TutorialListView.as_view(), name = 'home'),
    path('admin/', admin.site.urls),
    path('tutorials/',include('tutorials.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/welcome',views.WelcomePage.as_view(), name='welcome'),
    path('accounts/thanks',views.ThanksPage.as_view(), name = 'thanks'),
    path('accounts/login',views.LoginPage.as_view(),name="account_login"),
    path('accounts/signup',views.SignupPage.as_view(),name="account_signup"),
    
    
    
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)