# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20161116_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='linktype',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='party',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='party',
            name='shortname_en',
            field=models.CharField(max_length=10, null=True, verbose_name='shortname'),
        ),
        migrations.AddField(
            model_name='question',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text_en',
            field=models.TextField(null=True, verbose_name='text'),
        ),
        migrations.AddField(
            model_name='state',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
    ]
