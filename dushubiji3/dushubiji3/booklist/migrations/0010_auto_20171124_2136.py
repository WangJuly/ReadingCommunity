# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0009_user_uarticlenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uarticlenumber',
            field=models.IntegerField(),
        ),
    ]
