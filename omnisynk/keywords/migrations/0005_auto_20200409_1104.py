# Generated by Django 3.0.4 on 2020-04-09 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0004_auto_20200408_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 11, 4, 49, 684003, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='keywordsgenerationresults',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 11, 4, 49, 684937, tzinfo=utc)),
        ),
    ]
