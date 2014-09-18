# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicblog', '0009_auto_20140827_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='for_post',
            field=models.ForeignKey(to='basicblog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
