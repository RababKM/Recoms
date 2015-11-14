# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150914_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='email',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='facebook',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='instagram',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='twitter',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='website',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
