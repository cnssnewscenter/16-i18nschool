# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_auto_20150717_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_intro',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
