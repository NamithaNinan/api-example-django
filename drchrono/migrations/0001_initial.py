# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=20)),
                ('last_name', models.CharField(default=b'', max_length=20)),
                ('doctor', models.PositiveIntegerField(default=-1)),
                ('gender', models.CharField(default=b'Male', max_length=60)),
                ('date_of_birth', models.CharField(default=b'2017-08-27 20:02:05.881329', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('access_token', models.CharField(max_length=100)),
            ],
        ),
    ]
