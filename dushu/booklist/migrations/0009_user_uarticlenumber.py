# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0008_auto_20171124_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uarticlenumber',
            field=models.IntegerField(default=0),
        ),
    ]
