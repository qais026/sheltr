from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
		# url(r'^$', TemplateView.as_view(template_name='app/index.html'), name='index')
		# )