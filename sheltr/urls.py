from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.forms import ProviderSearchForm
from haystack.query import SearchQuerySet

from haystack.views import SearchView

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'sheltr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.urls')),
	url(r'^emails/', include('emails.urls')),
	url(r'^about/', 'app.views.about', name='about'),

	# THIS PAGE IS USING THE DEFAULT EXAMPLE PROVIDED IN THE HAYSTACK DOCS--ONLY TEMPORARY.
	url(r'^search/', include('haystack.urls')),
)

# urlpatterns += patterns('',
# 	url(r'^mysearch/', ProviderSearchView.as_view(), name="haystack_search"),
# )


# THIS PAGE IS WHAT WE WANT TO END UP USING AS IT ALLOWS CUSTOMIZABILITY.
urlpatterns += patterns('haystack.views',
    url(r'^mysearch/$', SearchView(
        template='search/search.html',
        form_class=ProviderSearchForm
    ), name='provider_search'),
)
