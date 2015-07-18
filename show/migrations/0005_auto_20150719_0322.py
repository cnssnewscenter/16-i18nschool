# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0004_teacher_teacher_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='hit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]
