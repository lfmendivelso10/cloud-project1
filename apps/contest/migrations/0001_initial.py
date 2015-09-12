# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'name')),
                ('image', models.CharField(max_length=250, verbose_name=b'image banner')),
                ('access_url', models.CharField(max_length=250, verbose_name=b'access URL')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name=b'start date')),
                ('end_date', models.DateTimeField(auto_now_add=True, verbose_name=b'end date')),
                ('prize_description', models.CharField(max_length=250, verbose_name=b'prize description')),
            ],
            options={
                'ordering': ['start_date', 'name'],
                'verbose_name': 'contest',
                'verbose_name_plural': 'contests',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name=b'first name')),
                ('last_name', models.CharField(max_length=100, verbose_name=b'last name')),
                ('email', models.CharField(max_length=100, verbose_name=b'email')),
                ('password', models.CharField(max_length=20, verbose_name=b'password')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250, verbose_name=b'description')),
                ('original_url', models.CharField(max_length=250, verbose_name=b'original url')),
                ('converted_url', models.CharField(max_length=250, verbose_name=b'converted url')),
                ('status', models.CharField(max_length=250, verbose_name=b'status')),
            ],
            options={
                'verbose_name': 'contest',
                'verbose_name_plural': 'contests',
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='contest.User')),
                ('organization', models.CharField(max_length=100, verbose_name=b'organization')),
            ],
            options={
                'ordering': ['organization', 'last_name', 'first_name'],
                'verbose_name': 'agent',
                'verbose_name_plural': 'agents',
            },
            bases=('contest.user',),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='contest.User')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
            bases=('contest.user',),
        ),
        migrations.AddField(
            model_name='video',
            name='owner',
            field=models.ForeignKey(related_name='videos', verbose_name=b'owner', to='contest.Client'),
        ),
        migrations.AddField(
            model_name='contest',
            name='agent',
            field=models.ForeignKey(related_name='contests', verbose_name=b'agent', to='contest.Agent'),
        ),
        migrations.AddField(
            model_name='client',
            name='contest',
            field=models.ForeignKey(related_name='clients', verbose_name=b'contest', to='contest.Contest'),
        ),
    ]
