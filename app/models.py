from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __unicode__(self):              
        return self.title

class Provider(models.Model):
    id = models.IntegerField(max_length=None, unique=True, primary_key=True)
    provider_name = models.CharField(max_length=128)
    location_name = models.CharField(max_length=128, null=True)
    image = models.CharField(max_length=128, null=True)
    website = models.CharField(max_length=128, null=True)
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=128)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.provider_name

    def __str__(self):
        return self.provider_name
