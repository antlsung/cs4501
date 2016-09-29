# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbay', '0002_auto_20160915_1956'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='users',
        ),
    ]
