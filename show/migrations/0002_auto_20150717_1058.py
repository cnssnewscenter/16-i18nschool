# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='intro',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='intro',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='pic',
            field=models.ImageField(blank=True, upload_to='teacher'),
        ),
    ]
