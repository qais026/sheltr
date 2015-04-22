from django.contrib import admin
from app.models import Provider, Category
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

class ProviderResource(resources.ModelResource):
    class Meta:
        model = Provider
        # ESSENTIAL LINES BELOW THAT AREN'T MENTIONED IN THE TUTORIAL 
        fields = ('id', 'provider_name', 'location_name', 'image', 'website', 'address1', 'address2', 'city', 'state', 'zipcode',)
    
class ProviderAdmin(ImportExportModelAdmin):
    resource_class = ProviderResource
    pass

admin.site.register(Category)
# Channing's comments:
# Also essential that ProviderAdmin is added as a second argument
# And in order to import csv there has to be an id column (I created
# a version of the csv called SheltrProvidersID.csv that works)
# also remember to add __str__ in order for names to show up on
# the admin module thing.
# MAIN ISSUE: Doesn't accept multiple providers of the same name
# POSSIBLE SOLUTION: recreate sheltr database where unique is no
# longer true for provider_name in models
admin.site.register(Provider, ProviderAdmin)
# Register your models here.

