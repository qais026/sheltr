from django.shortcuts import render
from django.contrib import messages
#from django.db.models import get_model
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError

from emails.models import EmailForm
#emails = models.ForeignKey(emails.EmailForm) 
#EmailForm = get_model('emails', 'models')
def sendmail(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			#botcheck = form.cleaned_data['botcheck'].lower()
			message = form.cleaned_data['message']
			fullemail = message + " " + firstname + " " + lastname + " " + "<" + email + ">"
			#Need to change receiver email
			send_mail(subject, fullemail, 'john.smith.dummy2@gmail.com' , ['john.smith.dummy2@gmail.com'], fail_silently = False)
			return HttpResponseRedirect('/emails/email/thankyou/')
		else:
			messages.add_message(request, messages.INFO, "Fields marked with an asterisk (*) are required.")
			return HttpResponseRedirect('/emails/email/')
	else:
		return HttpResponseRedirect('/emails/email1/') 
