# Generated by Django 2.0 on 2020-01-23 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='icon',
        ),
    ]
