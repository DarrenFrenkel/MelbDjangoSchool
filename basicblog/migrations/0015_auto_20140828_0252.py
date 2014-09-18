# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicblog', '0014_auto_20140828_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='for_post',
            field=models.ForeignKey(to='basicblog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
