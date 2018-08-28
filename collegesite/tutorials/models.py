from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from accounts.models import Membership


# Create your models here.
User = get_user_model()


class Course(models.Model):
	title = models.CharField(max_length=200)
	lecturer = models.ForeignKey(User,related_name="courses",on_delete=models.SET_NULL,null=True)
	membership = models.ManyToManyField(Membership)
	description = models.TextField()
	cover_image = models.FileField(upload_to='lectures/cover_photos')
	slug = models.SlugField(allow_unicode=True,unique=True,editable=False)
	created_at = models.DateTimeField(auto_now =True)
	resources = models.FileField(upload_to='resources/',default = 'null', blank = True, null=True)
	prize = models.FloatField()
	def save(self,*args,**kwargs):
		self.slug = slugify(self.title)
		super().save(*args,**kwargs)
		
	def __str__(self):
		return self.title 

	
	
class Tutorial(models.Model):
	topic = models.CharField(max_length=200)
	course = models.ForeignKey(Course,related_name="tutorials",on_delete=models.SET_NULL,null=True)
	video = models.FileField(upload_to='lectures/',null=True,blank=True)
	position=models.IntegerField()
	length = models.CharField(max_length=10)
	
	def __str__(self):
		return self.topic
	
	
	class Meta:
		ordering =['position']
		
#	def get_absolute_url(self):
#		return reverse('tutorial:single',kwargs={'username':self.user.username,'slug':self.slug})	
	
	
	
class Registered_student(models.Model):
	course=models.ForeignKey(Course,related_name='enrolled_students',on_delete=models.PROTECT,null=True)
	student = models.ForeignKey(User,related_name='enrolled_tutorial',on_delete=models.SET_NULL,null=True)
	enrolled_at = models.DateTimeField(auto_now = True)
	
	class Meta:
		unique_together =['student','course']
	
	def __str__(self):
		return self.course.title
	
	

	
	



	