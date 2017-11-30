# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0013_staruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staruser',
            name='staruserauthor',
            field=models.CharField(verbose_name='收藏者', max_length=50),
        ),
    ]
