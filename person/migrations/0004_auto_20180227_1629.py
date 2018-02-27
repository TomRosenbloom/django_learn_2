# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 16:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20180213_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='partial_date',
        ),
        migrations.AddField(
            model_name='person',
            name='birth_month',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='birth_year',
            field=models.PositiveIntegerField(blank=True, help_text='Use format YYYY', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2018)]),
        ),
    ]