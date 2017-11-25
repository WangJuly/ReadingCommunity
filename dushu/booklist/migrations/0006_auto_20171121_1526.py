# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0005_user_ulbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('atitle', models.CharField(verbose_name='笔记标题', max_length=30)),
                ('aauthor', models.CharField(verbose_name='笔记作者', max_length=30)),
                ('abookname', models.CharField(verbose_name='书籍名称', max_length=30)),
                ('awriter', models.CharField(verbose_name='书籍作者', max_length=30)),
                ('acontent', models.CharField(verbose_name='笔记正文', max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='book',
        ),
    ]
