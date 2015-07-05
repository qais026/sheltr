import datetime
from haystack import indexes
from .models import Provider

class ProviderIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)

	#Whenever you change these you need to run build_solr_schema again and move the schema file to the appropriate location.
	#Also, restart the Solr server for changes to take place.
	provider_name = indexes.CharField(model_attr='provider_name')
	address1 = indexes.CharField(model_attr='address1')


	def get_model(self):
		return Provider

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter()