# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150906_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
    ]
