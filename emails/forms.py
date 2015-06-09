#The forms.py file will hold forms. These forms can be based on the
#models created in models.py or they can be custom model-less forms.

#You can create form validators by overriding the function
	#def clean_field(self):
#for each field in a form. Note that this will retain the field property validators
#for example in an email field it will still verify that is in a proper
#email format.

from django import forms
#Since the form we want to make for people to sign up an email is
#based on the EmailSignUp model, we want to import the model here.
from .models import EmailSignUp

#EmailForm class that inherits forms.ModelForm. A ModelForm is a form
#based on a model, which you will define. 
class EmailForm(forms.ModelForm):
	#In a ModelForm class you define what model you are building a form
	#upon by using class Meta as shown below. Define what fields you
	#want to be shown on the form.
	class Meta:
		model = EmailSignUp
		fields = ['your_name', 'email', 'subject', 'message']

	#This cleans up the email field after the form is submitted. If
	#the fild does not meet certain critera, you can alter the input
	#so that it does or you can raise a validation error with a message
	#telling the user the error.
