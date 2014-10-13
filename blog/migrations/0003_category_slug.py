# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141010_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, unique=True, default='testcat'),
            preserve_default=False,
        ),
    ]
