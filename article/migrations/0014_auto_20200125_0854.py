# Generated by Django 2.0 on 2020-01-25 00:54

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20200125_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='内容'),
        ),
    ]