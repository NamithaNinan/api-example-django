# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0002_auto_20170827_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patient', models.PositiveIntegerField(default=-1)),
                ('status', models.CharField(default=b'', max_length=20)),
                ('duration', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.CharField(default=b'2017-08-30 08:27:48.704891', max_length=10),
        ),
    ]
