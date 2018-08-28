from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings


def send_email(request):
	if request.method == 'POST':
		email_from = request.POST.get('email')
	
		email_message = request.POST.get('message')
		email_sender = request.POST.get('')
		
		subject = 'From my website'
	
		to_list = [settings.EMAIL_HOST_USER,]
		from_email = email_from
		message = email_message
		send_mail(subject,message,from_email,to_list,fail_silently=True)
	
	
		
	return redirect('home')			
			