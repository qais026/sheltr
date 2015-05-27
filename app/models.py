from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __unicode__(self):              
        return self.category_name

class Provider(models.Model):
    # blank=True necessary to allow for incomplete data entry edits
    # makes it so the field is NOT required
    id = models.IntegerField(max_length=None, unique=True, primary_key=True)
    provider_name = models.CharField(max_length=128)
    location_name = models.CharField(max_length=128, null=True, blank=True)
    image = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=128, null=True, blank=True)
    address1 = models.CharField(max_length=128, blank=True)
    address2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    zipcode = models.CharField(max_length=128, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.provider_name

    def __str__(self):
        return self.provider_name
