# Generated by Django 2.1.8 on 2020-01-02 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSendLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailto', models.CharField(max_length=300, verbose_name='收件人')),
                ('title', models.CharField(max_length=2000, verbose_name='邮件标题')),
                ('content', models.TextField(verbose_name='邮件内容')),
                ('send_result', models.BooleanField(default=False, verbose_name='结果')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '邮件发送log',
                'verbose_name_plural': '邮件发送log',
                'ordering': ['-created_time'],
            },
        ),
    ]