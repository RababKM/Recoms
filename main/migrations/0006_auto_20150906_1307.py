# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150906_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image10',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image2',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image3',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image4',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image5',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image6',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image7',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image8',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='image9',
            field=models.ImageField(upload_to=b'recommendations', blank=True),
        ),
    ]
