# Generated by Django 2.0 on 2020-01-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('desc', models.CharField(max_length=256, verbose_name='简介')),
                ('content', models.TextField(verbose_name='内容')),
                ('date', models.DateField(auto_now=True, verbose_name='发表日期')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击量')),
                ('love_num', models.IntegerField(default=0, verbose_name='点赞量')),
                ('image', models.ImageField(upload_to='uploads/article/%Y/%m/%d', verbose_name='文章图片')),
            ],
            options={
                'verbose_name': '文章表',
                'verbose_name_plural': '文章表',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签表',
                'verbose_name_plural': '标签表',
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='article.Tag', verbose_name='标签'),
        ),
    ]
