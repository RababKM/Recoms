# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_recommendation_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='phone_number',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='telephone',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
