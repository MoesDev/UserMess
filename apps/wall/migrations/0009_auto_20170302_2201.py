# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 04:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0008_auto_20170302_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user_id',
            new_name='user',
        ),
    ]