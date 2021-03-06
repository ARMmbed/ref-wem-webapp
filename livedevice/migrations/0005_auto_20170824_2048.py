"""
mbed tools
Copyright (c) 2018 ARM Limited
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livedevice', '0004_auto_20170824_2042'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='wemSite',
            new_name='SiteScheme',
        ),
    ]
