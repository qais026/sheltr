# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150422_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='address1',
            field=models.CharField(max_length=128),
        ),
    ]
