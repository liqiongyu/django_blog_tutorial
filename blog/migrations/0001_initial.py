# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u535a\u5ba2\u6807\u9898')),
                ('category', models.CharField(max_length=50, verbose_name='\u535a\u5ba2\u6807\u7b7e', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('content', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
