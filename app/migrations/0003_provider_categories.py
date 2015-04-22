# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='categories',
            field=models.ManyToManyField(to='app.Category'),
            preserve_default=True,
        ),
    ]
