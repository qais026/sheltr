from django.shortcuts import render
from django.contrib import messages
#from django.db.models import get_model
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError

from .forms import EmailForm
#emails = models.ForeignKey(emails.EmailForm) 
#EmailForm = get_model('emails', 'models')

def sendmail(request):
	form = EmailForm(request.POST or None)
	context = {
		"required": "This field is required.",
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		# instance.save()
		name = form.cleaned_data['your_name']
		email = form.cleaned_data['email']
		subject = form.cleaned_data['subject']
		message = form.cleaned_data['message']
		fullemail = message + " " + firstname + " " + lastname + " " + "<" + email + ">"
		#Need to change receiver email
		send_mail(subject, fullemail, 'mapitherebmore@gmail.com' , ['mapitherebmore@gmail.com'], fail_silently = False)
		return HttpResponseRedirect('/emails/email/thankyou/')
	
	#else:
	#	messages.add_message(request, messages.INFO, "Fields marked with an asterisk (*) are required.")
	#	return render(request, "emails/email.html", context)

	return render(request, "emails/email.html", context)

