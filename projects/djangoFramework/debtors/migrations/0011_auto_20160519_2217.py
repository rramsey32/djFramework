# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 03:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('debtors', '0010_auto_20160519_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 20, 3, 17, 31, 10134, tzinfo=utc), verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='crime',
            name='judgement_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 20, 3, 17, 31, 10134, tzinfo=utc), verbose_name='date of judgement'),
        ),
        migrations.AlterField(
            model_name='crime',
            name='offense_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 20, 3, 17, 31, 10134, tzinfo=utc), verbose_name='date of offense'),
        ),
        migrations.AlterField(
            model_name='crime',
            name='sentence_start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 20, 3, 17, 31, 10134, tzinfo=utc), verbose_name='date of sentence start'),
        ),
        migrations.AlterField(
            model_name='crime',
            name='sentence_stop_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 20, 3, 17, 31, 10134, tzinfo=utc), verbose_name='date of sentence stop'),
        ),
    ]
