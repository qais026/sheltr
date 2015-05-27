# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_provider_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='id',
            field=models.IntegerField(serialize=False, unique=True, primary_key=True),
        ),
    ]
