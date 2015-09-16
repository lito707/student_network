# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rsrc_type', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(verbose_name=b'created_at')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
