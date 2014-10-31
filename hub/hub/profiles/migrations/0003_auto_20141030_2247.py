# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20141030_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='dockeruser',
            name='is_admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dockeruser',
            name='email',
            field=models.EmailField(default='foo@bar.com', unique=True, max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dockeruser',
            name='is_staff',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
