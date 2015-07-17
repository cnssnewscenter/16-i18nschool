# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_auto_20150717_1058'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.AddField(
            model_name='teacher',
            name='course',
            field=models.CharField(max_length=256, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='school',
            field=models.CharField(max_length=256, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='school_own',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
    ]
