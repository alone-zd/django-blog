# Generated by Django 2.0 on 2020-01-25 02:39

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20200125_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='内容'),
        ),
    ]