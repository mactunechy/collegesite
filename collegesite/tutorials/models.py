from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
User = get_user_model()
class Tutorial(models.Model):
	topic = models.CharField(max_length=200)
	lecturer = models.ForeignKey(User,related_name='tutorials')
	description = models.TextField()
	prize = models.IntegerField()
	cover_image = models.FileField(upload_to='lectures/cover_photos')
	video = models.FileField(upload_to='lectures/',null=True,blank=True)
	resources = models.FileField(upload_to='resources/',default = 'null', blank = True, null=True)
	registered_students = models.ManyToManyField(User,through='Registered_students')
	slug = models.SlugField(allow_unicode=True,unique=True,editable=False)
	created_at = models.DateTimeField(auto_now =True)
	
	def save(self,*args,**kwargs):
		self.slug = slugify(self.topic)
		super().save(*args,**kwargs) 
	
	class Meta:
		ordering =['-created_at']
		
	def get_absolute_url(self):
		return reverse('tutorial:single',kwargs={'username':self.user.username,'slug':self.slug})	
	
	
	
class Registered_students(models.Model):
	tutorial = models.ForeignKey(Tutorial,related_name = 'enrolled_students',on_delete = models.PROTECT)
	student = models.ForeignKey(User,related_name='enrolled_tutorial',on_delete = models.PROTECT)
	enrolled_at = models.DateTimeField(auto_now = True)
	
	