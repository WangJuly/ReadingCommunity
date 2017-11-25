# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0007_auto_20171121_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='acontent',
            field=models.TextField(verbose_name='笔记正文', max_length=10000),
        ),
    ]
