# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-27 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False, verbose_name='번호')),
                ('paymentDate', models.DateField(default=django.utils.timezone.now, verbose_name='결제일')),
                ('paymentType', models.CharField(choices=[('카드', '카드'), ('현금', '현금')], default='카드', max_length=6, verbose_name='결제방식')),
                ('paymentState', models.CharField(choices=[('결제', '결제'), ('환불', '환불')], default='결제', max_length=6, verbose_name='결제상태')),
                ('item', models.CharField(max_length=30, null=True, verbose_name='수업/상품')),
                ('price', models.IntegerField(blank=True, default=0, verbose_name='가격')),
                ('note', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Memo')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Student', verbose_name='학생')),
            ],
        ),
    ]
