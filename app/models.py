from django.db import models


# Create your models here.

class Category(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    category_name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):              
        return self.category_name

    def __str__(self):
        return self.category_name

class Provider(models.Model):
    # blank=True necessary to allow for incomplete data entry edits
    # makes it so the field is NOT required
    id = models.AutoField(unique=True, primary_key=True)
    provider_name = models.CharField(max_length=128)
    location_name = models.CharField(max_length=128, null=True, blank=True)
    image = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=128, null=True, blank=True)
    address1 = models.CharField(max_length=128, blank=True)
    address2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    zipcode = models.CharField(max_length=128, blank=True)
    """categories = models.ManyToManyField(Category, blank=True)     
    contact = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)
    hours = models.CharField(max_length=128, blank=True)
    agency_description = models.CharField(max_length=128, blank=True)
    eligibity = models.CharField(max_length=128, blank=True)
    fee_structure_source = models.CharField(max_length=128, blank=True)
    application_process = models.CharField(max_length=128, blank=True)
    documents_required = models.CharField(max_length=128, blank=True)
    details = models.CharField(max_length=128, blank=True)
    details_continued = models.CharField(max_length=128, blank=True)
    services = models.ForeignKey(Services, blank=True)"""

    def __unicode__(self):
        return self.provider_name

    def __str__(self):
        return self.provider_name
