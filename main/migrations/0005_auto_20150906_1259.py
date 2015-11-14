# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150906_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='telephone',
            field=models.CharField(max_length=13, blank=True),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='phone_number',
            field=models.CharField(default=2, max_length=13, blank=True),
            preserve_default=False,
        ),
    ]
