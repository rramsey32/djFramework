# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debtors', '0012_auto_20160522_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='debtor',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='debtor',
            name='debtor_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
