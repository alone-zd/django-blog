# Generated by Django 2.0 on 2020-01-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200123_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='发表日期'),
        ),
    ]
