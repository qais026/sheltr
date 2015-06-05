# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150422_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='address1',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='address2',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='categories',
            field=models.ManyToManyField(to='app.Category', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='city',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='image',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='location_name',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='state',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='website',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='zipcode',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
