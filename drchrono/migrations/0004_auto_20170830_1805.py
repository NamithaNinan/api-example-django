# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0003_auto_20170830_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='scheduled_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 30, 18, 5, 54, 375137), blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.CharField(default=b'2017-08-30 18:05:54.374088', max_length=10),
        ),
    ]
