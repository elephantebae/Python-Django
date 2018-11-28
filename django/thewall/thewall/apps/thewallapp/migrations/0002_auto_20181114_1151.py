# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-14 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('thewallapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='users_who_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_from_users', to='thewallapp.Users'),
        ),
        migrations.AddField(
            model_name='comments',
            name='message_with_comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_comments', to='thewallapp.Messages'),
        ),
        migrations.AddField(
            model_name='comments',
            name='users_who_comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='thewallapp.Users'),
        ),
    ]
