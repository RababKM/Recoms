# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150914_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='youtube',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
