from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView


from emails.views import sendmail

urlpatterns = patterns('',
	
	#Home page for contact page based on template found in home.html
	url(r'^$', TemplateView.as_view(template_name='emails/home.html'), name='home'),
	
    url(r'^email/thankyou/$', TemplateView.as_view(template_name='emails/thankyou.html'), name='thankyou'),
    url(r'^email/$', sendmail, name='email'),
)
