# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 10:59
from __future__ import unicode_literals

import django.contrib.sites.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_set_site_domain_and_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='domain',
            field=models.CharField(max_length=100, unique=True, validators=[django.contrib.sites.models._simple_domain_name_validator], verbose_name='domain name'),
        ),
    ]
