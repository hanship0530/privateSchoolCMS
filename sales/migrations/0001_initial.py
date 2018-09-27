# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-27 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monthsale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='월')),
                ('sales', models.IntegerField(null=True, verbose_name='월 매출')),
                ('refundsCounts', models.IntegerField(null=True, verbose_name='환불 횟수')),
                ('paymentsCounts', models.IntegerField(null=True, verbose_name='결제 횟수')),
            ],
        ),
    ]
