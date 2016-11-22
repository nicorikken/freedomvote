# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20161116_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='politician',
            name='state',
        ),
        migrations.AddField(
            model_name='politician',
            name='state',
            field=models.ManyToManyField(to='core.State', null=True, verbose_name='state', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_number',
            field=models.IntegerField(verbose_name='question_number'),
        ),
    ]
