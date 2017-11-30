# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0010_auto_20171124_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('suname', models.CharField(verbose_name='收藏用户', max_length=50)),
                ('stitle', models.CharField(verbose_name='收藏笔记的标题', max_length=30)),
                ('sauthor', models.CharField(verbose_name='收藏笔记的作者', max_length=30)),
                ('sbookname', models.CharField(verbose_name='收藏笔记的书籍名称', max_length=30)),
                ('swriter', models.CharField(verbose_name='收藏笔记的书籍作者', max_length=30)),
                ('scontent', models.TextField(verbose_name='收藏笔记的正文', max_length=10000)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='uarticlenumber',
        ),
    ]
