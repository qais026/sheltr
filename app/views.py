from django.http import HttpResponse
from django.shortcuts import render

from haystack.query import SearchQuerySet
from haystack.generic_views import SearchView
from haystack.forms import ModelSearchForm

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'app/index.html', context_dict)

def about(request):
	context = {}
	return render(request, 'sheltr/about.html', context)

def search(request):
	form = ProviderSearchForm(request.POST or None)
	context = {
		"form": form,
	}

#Trying the "new" way:

# class ProviderSearchView(SearchView):

# 	template_name = "search/search.html"
# 	queryset = SearchQuerySet().all()
# 	form_class = ModelSearchForm

# 	def get_queryset(self):
# 		queryset = super(ProviderSearchView, self).get_queryset()
# 		# further filter queryset based on some set of criteria
# 		return queryset

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(ProviderSearchView, self).get_context_data(*args, **kwargs)
# 		# do something
# 		return context
