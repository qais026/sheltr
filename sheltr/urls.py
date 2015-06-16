from django.conf.urls import patterns, include, url
from django.contrib import admin

from app import views

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'sheltr.views.home', name='home'), WAS ORIGINALLY INCLUDED IN THE PULL
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.urls')),
	url(r'^emails/', include('emails.urls')),
    
    url(r'^$', views.index, name='index'), # added this from my branch
    url(r'search/', include('haystack.urls'))
)
