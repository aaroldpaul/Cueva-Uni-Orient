# Generated by Django 3.2.6 on 2021-12-15 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0002_auto_20211215_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='password',
        ),
    ]
