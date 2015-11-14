# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('info', models.TextField(null=True)),
                ('map_img', models.ImageField(upload_to=b'maps', blank=True)),
                ('image', models.ImageField(upload_to=b'recommendations')),
                ('phone_number', models.CharField(max_length=13, null=True)),
            ],
        ),
    ]
