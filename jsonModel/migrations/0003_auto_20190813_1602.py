# Generated by Django 2.2.3 on 2019-08-13 16:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsonModel', '0002_auto_20190813_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsonmodel',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
