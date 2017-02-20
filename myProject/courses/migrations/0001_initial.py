# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('assessment_id', models.AutoField(serialize=False, primary_key=True)),
                ('assessment_type', models.CharField(max_length=100)),
                ('max_point', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('course_number', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('major', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enrollment_id', models.AutoField(serialize=False, primary_key=True)),
                ('grade', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GradeCriteria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('range_start', models.IntegerField()),
                ('range_end', models.IntegerField()),
                ('grade', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('point', models.IntegerField(blank=True, null=True)),
                ('assessment', models.ForeignKey(to='courses.Assessment')),
                ('enrollment', models.ForeignKey(to='courses.Enrollment')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('section_number', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('course', models.ForeignKey(to='courses.Course')),
                ('instructor', models.ForeignKey(to='accounts.Instructor')),
            ],
        ),
        migrations.AddField(
            model_name='gradecriteria',
            name='section',
            field=models.ForeignKey(to='courses.Section'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='section',
            field=models.ForeignKey(to='courses.Section'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='enrollment',
            field=models.ForeignKey(to='courses.Enrollment'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='section',
            field=models.ForeignKey(to='courses.Section'),
        ),
    ]
