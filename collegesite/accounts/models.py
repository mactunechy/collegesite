from django.db import models
from django.shortcuts import redirect
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
PLAN_CHOICES= (
('Free','Free'),
('pro','Professional'),
('ent','Enterprise'))	

class Membership(models.Model):
	plan = models.CharField(choices=PLAN_CHOICES,max_length=50)
	prize = models.IntegerField()
	
	def __str__(self):
		return self.plan



	
class Profile(models.Model):
	user = models.OneToOneField(User,related_name="profile",on_delete=models.SET_NULL,null=True)
	profile_pic = models.FileField(upload_to='profile')
	membership = models.ForeignKey(Membership,related_name="users",on_delete=models.SET_NULL,null=True)		
	
	def __str__(self):
		return self.name
		
		
	def get_absolute_url(self):
		return redirect('home')	
		
		
	