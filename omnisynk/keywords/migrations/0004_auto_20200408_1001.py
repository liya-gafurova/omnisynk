# Generated by Django 3.0.4 on 2020-04-08 10:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0003_auto_20200408_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywordsgenerationresults',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 10, 1, 31, 319002, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='keywordsgenerationresults',
            name='id_example',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='keywords.Example'),
        ),
        migrations.AddField(
            model_name='keywordsgenerationresults',
            name='keywords',
            field=models.CharField(default='null', max_length=4000),
        ),
        migrations.AddField(
            model_name='keywordsgenerationresults',
            name='method_name',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='example',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 10, 1, 31, 317829, tzinfo=utc)),
        ),
    ]