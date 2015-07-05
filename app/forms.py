from django import forms
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
from .models import Provider


class ProviderSearchForm(SearchForm):

	location_name = forms.CharField(required=False)
	category = forms.CharField(required=False)


	def search(self):
		# First, store the SearchQuerySet received from other processing.
		sqs = super(ProviderSearchForm, self).search()

		if not self.is_valid():
			return self.no_query_found()

		# if self.cleaned_data['category']:
		# 	sqs = sqs.filter(category_name__startswith=self.cleaned_data['category'])
		# 	return sqs
	

		if self.cleaned_data['location_name']:
			sqs = sqs.filter(address1=self.cleaned_data['location_name'])

		return sqs