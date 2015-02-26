# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(unique=True, max_length=128)),
                ('location_name', models.CharField(null=True, max_length=128)),
                ('image', models.CharField(null=True, max_length=128)),
                ('website', models.CharField(null=True, max_length=128)),
                ('address1', models.CharField(max_length=128)),
                ('address2', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
