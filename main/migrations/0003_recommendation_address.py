# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150906_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
