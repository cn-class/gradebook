# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('instructor_id', models.IntegerField(serialize=False, primary_key=True)),
                ('degree', models.CharField(max_length=100)),
                ('instructor_picture', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]
