from django.contrib import admin
from app.models import Provider, Category
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    pass

class ProviderResource(resources.ModelResource):
    class Meta:
        model = Provider 
        #fields = ('id', 'provider_name', 'location_name', 'image', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'resources')
    
class ProviderAdmin(ImportExportModelAdmin):
    resource_class = ProviderResource
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Provider, ProviderAdmin)
