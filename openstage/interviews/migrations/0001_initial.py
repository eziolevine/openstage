# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 11:57
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DateMixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('date_modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Inerview',
            fields=[
                ('datemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='interviews.DateMixin')),
                ('publisher_is_draft', models.BooleanField(db_index=True, default=True, editable=False)),
                ('publisher_modified_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('publisher_published_at', models.DateTimeField(editable=False, null=True)),
                ('slug', models.SlugField()),
                ('video', embed_video.fields.EmbedVideoField()),
                ('title', models.CharField(max_length=500)),
                ('interviewee', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publisher_linked', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publisher_draft', to='interviews.Inerview')),
            ],
            options={
                'abstract': False,
                'permissions': (('can_publish', 'Can publish'),),
            },
            bases=('interviews.datemixin', models.Model),
            managers=[
                ('publisher_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
