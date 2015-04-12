from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView


from emails.views import sendmail

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='emails/home.html'), name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    #url(r'^admin/', include(admin.site.urls)),
	
    url(r'^email/send/$', sendmail),
    url(r'^email/thankyou/$', TemplateView.as_view(template_name='emails/thankyou.html'), name='thankyou'),
    url(r'^email/$', TemplateView.as_view(template_name='emails/email.html'), name='email'),
)
