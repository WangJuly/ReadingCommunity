# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0011_auto_20171128_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='star',
            name='sauthor',
        ),
        migrations.RemoveField(
            model_name='star',
            name='sbookname',
        ),
        migrations.RemoveField(
            model_name='star',
            name='scontent',
        ),
        migrations.RemoveField(
            model_name='star',
            name='swriter',
        ),
    ]
