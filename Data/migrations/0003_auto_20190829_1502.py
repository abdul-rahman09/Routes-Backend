# Generated by Django 2.2.3 on 2019-08-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0002_data_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]