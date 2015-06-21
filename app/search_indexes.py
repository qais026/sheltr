import datetime
from haystack import indexes
from .models import Provider

class ProviderIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    provider_name = indexes.CharField(model_attr='provider_name')
    location_name = indexes.CharField(model_attr='location_name')

    def get_model(self):
        return Provider

    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())