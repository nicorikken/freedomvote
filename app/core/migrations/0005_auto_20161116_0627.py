# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161114_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_number',
            field=models.IntegerField(verbose_name='Vraag nummer'),
        ),
    ]
