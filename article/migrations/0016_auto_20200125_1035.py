# Generated by Django 2.0 on 2020-01-25 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20200125_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
    ]
