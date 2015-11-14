# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('info', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='recommendation',
            name='category',
            field=models.ForeignKey(to='main.Category', null=True),
        ),
    ]
