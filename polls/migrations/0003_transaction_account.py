# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_transaction_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='polls.Account'),
        ),
    ]
