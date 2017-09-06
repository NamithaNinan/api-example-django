# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0004_auto_20170830_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='dr_seeing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='dr_seeing_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 30, 18, 18, 39, 729210), blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.CharField(default=b'2017-08-30 18:18:39.728187', max_length=10),
        ),
    ]
