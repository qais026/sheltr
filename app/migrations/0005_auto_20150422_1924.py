# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150422_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='address1',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_name',
            field=models.CharField(max_length=128),
        ),
    ]
