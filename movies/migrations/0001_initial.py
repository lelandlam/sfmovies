# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('release_year', models.CharField(max_length=120)),
                ('locations', models.CharField(max_length=120)),
                ('production_company', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
