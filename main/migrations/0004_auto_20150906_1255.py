# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_recommendation_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='image',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
    ]
