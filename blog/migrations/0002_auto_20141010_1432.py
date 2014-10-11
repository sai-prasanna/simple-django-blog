# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories', 'verbose_name': 'Category', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category', related_name='posts', null=True),
        ),
    ]
