# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testModels', '0003_auto_20140915_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporter',
            name='num_of_articles',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
